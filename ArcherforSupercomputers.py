import unittest
from loopsdic import mydict
from pyosl import Factory
from uuid import uuid4
from pyosl.tools import named_build, calendar_period, osl_fill_from, online, numeric_value, get_reference_for, new_document
from pyosl.tools import osl_encode2json, bundle_instance, Triples, Triples2
from pyosl.uml import TriplesDelux
from rdflib.serializer import Serializer

from rdflib.extras.external_graph_libs import rdflib_to_networkx_graph

import networkx as nx
import matplotlib.pyplot as plt
from networkx import Graph as NXGraph
import collections
import statistics
import math
import rdflib

#import PyPDF2 
#import glob
#from natsort import natsorted

def make_hpc(item, author):
    """
    Makes a PYOSL instance of an HPC deescription from a set of attributes held in an external dictionary
    :param item: specific HPC instance as a dictionary of attributes
    :param author: pyosl author instance
    :return: PYOSL instance of that HPC description.
    """

    def whatami(parent, attribute):
        """ Introspect attribute of parent to find out what type it is, even if the current value is None.
        Tell me if I'm not a valid attribute of the parent."""
        properties = {x[0]: x[1] for x in parent._osl.properties + parent._osl.inherited_properties}
        try:
            p = properties[attribute]  # this will raise a key error if attribute not in (expected) properties
            if 'linked_to' in p:   # we need to avoid the linked_to(x) syntax
                return p[10:-1]
            else:
                return p
        except KeyError:
            raise ValueError(f'{attribute} not a valid attribute for {parent}') from None

    def assign_value(parent, attribute, value):
        """ Handle assigning values in the situation where the value may in fact be a list of values, or
        a list of values each of which is described by a dictionary."""

        def unpack(p, kk, vv):
            """ Unpack a value vv of p corresponding to attribute kk."""
            if isinstance(vv, dict):
                avalue = Factory.build(whatami(p, kk))
                # if it's a document, we need to sort out the minimal metadata
                if avalue._osl.is_document:
                    avalue._meta.uid = str(uuid4())
                    avalue._meta.author = author
                # and then loop over all the attributes described in the dictionary
                for k, v in vv.items():
                    whatami(avalue, k)  # alert invalid attributes
                    assign_value(avalue, k, v)
                return avalue
            # nothing to unpack, just use it as is:
            return vv

        if isinstance(value, list):
            
 # if the thing im loolik at the is value is a list then unpack each item  in eh list then set into to setattr :
                
            vals = [unpack(parent, attribute, v) for v in value]
            setattr(parent, attribute, vals)
        else:
            setattr(parent, attribute, unpack(parent, attribute, value))

    assert 'name' in item, "All top level items must have a platform name"
    hpc = new_document('platform.machine', item['name'], author=author)
    
    for k, v in item.items():
        whatami(hpc, k)  # alert invalid attributes
        assign_value(hpc, k, v)

    return hpc


def shells_with_adjacent_layout(G, root):
    """ Provides and populates a canvas of node positions for a networkx
    graph, [[G]] in shells around a central [[root]] node. Returns a dictionary
    of nodes positions keyed from node name."""

    class Slot:
        def __init__(self, a, x, y):
            self.a, self.x, self.y = a, x, y
            self.used = False

    class Slots:
        """ Set up the list of possible places for a node to be """

        def __init__(self, rank_sizes, radius=1.5, scale=1.0):
           
            self.radius, self.scale = radius, scale
            self.slots = [[Slot(0, 0.0, 0.0), ], ]
            for i, size in enumerate(rank_sizes[1:]):
                self.slots.append(self.get_slots(i + 1, size))
            self.nodes = {}
            self.rank_delta = [0, ]
            for rnk in range(len(rank_sizes))[1:]:
                self.rank_delta.append(self.slots[rnk][1].a - self.slots[rnk][0].a)

        def get_slots(self, index, n):
            """ Get [[n]] slots for [[index]] shell"""

            def getxy(i, n, radius, offset=0):
                """ Get the ith slot of n at distance radius from origin starting from offset radians """
                angle = offset + i * 2 * math.pi / n
                x = math.sin(angle) * radius
                y = math.cos(angle) * radius
                return Slot(angle, x, y)

            r = self.radius * self.scale * index
            return [getxy(i, n, r) for i in range(n)]

        def add_node(self, node, rank, inner_node=None):
            """ Place node in unused slot in rank,
            if inner_node present, attempt to place near in angle terms to inner_node"""
            if inner_node:
                if rank < 2:
                    raise ValueError("Cannot use inner_node option for ranks less than 2")
                try:
                    first_guess = self.nodes[inner_node].a
                except KeyError:
                    raise ValueError(f'Attempt to use inner_node ({inner_node}) not seen before')
                ip = round(first_guess / self.rank_delta[rank])
                for s in self.slots[rank][ip:]:
                    if not s.used:
                        s.used = True
                        self.nodes[node] = s
                        return
                for s in reversed(self.slots[rank][0:ip]):
                    if not s.used:
                        self.nodes[node] = s
                        return
            else:
                for s in self.slots[rank]:
                    if not s.used:
                        s.used = True
                        self.nodes[node] = s
                        return
            raise ValueError(f'Unable to insert f{node} into rank {rank}')

    ranks = [[root], list(G.neighbors(root)),]
    collected = ranks[0]+ranks[1]
    ranks.append([])
    current = 2
    while len(collected) < len(G.nodes()):
        for s in ranks[current-1]:
            nodes = G.neighbors(s)
            for n in nodes:
                if n not in collected:
                    ranks[current].append(n)
                    collected.append(n)
        current += 1

    rank_sizes = [len(rank) for rank in ranks]
    if len(rank_sizes) > 4:
        nn = len(G.nodes())
        raise ValueError(f'This code not suitable for {nn} nodes')

    possible_sizes = [1, 8, 24, 48]
    placement_sizes = [max(n,p) for n,p in zip(rank_sizes, possible_sizes)]

    allslots = Slots(placement_sizes)

    for i in range(len(ranks)):
        if i > 1:
            # do it as adjacencies from inner rank
            for n in ranks[i-1]:
                edges = G.edges(n)
                for s,o in edges:
                    print('edge',s, o)
                    if o not in allslots.nodes:
                        allslots.add_node(o, i, inner_node=n)
        else:
            for node in ranks[i]:
                allslots.add_node(node, i)

    return {k: (v.x, v.y) for k,v in allslots.nodes.items()}


class Viewer:
    def __init__(self, instance):
        self.ts = Triples2()
        #triples s, p ,o 
        self.ts.add_instance(instance)
        self.clean_triples = [(self._clean(i), self._cleanp(j), self._clean(k))
                         for i, j, k in self.ts.semantic_triples]
        self.docs = [self._clean(n) for n in self.ts.semantic_nodes['shared.doc_reference']]
        self.urls = [self._clean(n) for n in self.ts.semantic_nodes['shared.online_resource']]
        
       # self.others= [self.clean(n) for n in self.others.ts.semantic_nodes['operating_system']]
                 
        # removing duplicates as we go
        subjects = list(dict.fromkeys([a for a,b,c in self.clean_triples]))
        objects = list(dict.fromkeys([c for a,b,c in self.clean_triples]))
        nodes = list(dict.fromkeys(subjects+objects))
        self.others = [x for x in nodes if str(x) not in self.docs+self.urls]
         
            
    def _clean(self, s):
        """ Used to clean up node names """
        if s.find('(') != -1:
            s = s[0:s.find('(')].rstrip(' ')
        return "{}".format(s.replace(' ', '\n').replace('https://', ''))

    def _cleanp(self, s):
        """ Used to clean predicates """
        return s.replace('_', '\n')

    def view_nx(self, root, name='{name}.pdf', layout='adjacent'):
        """ Use nx, experimental code """
        G = nx.MultiDiGraph()
        G.add_edges_from([(i, k) for i, j, k in self.clean_triples])
       # G.add_nodes_from
       

        if layout == 'adjacent':
            pos = shells_with_adjacent_layout(G, root)
        elif layout == 'kamada':
            pos = nx.kamada_kawai_layout(G, scale=2)
        else:
            raise ValueError(f'Unknown layout option {layout}')

        otherlabels = {n: n for n in self.others}
        doclabels = {n: n for n in self.docs}
        urllabels = {n: n for n in self.urls}

        fig, ax = plt.subplots(figsize=(12, 12))
        ax.set_xlim((-6, 6))
        ax.set_ylim((-6, 6))

        nx.draw_networkx_nodes(G, pos, self.others, node_size=5800, node_color='lightcoral')
        nx.draw_networkx_labels(G, pos, otherlabels, font_size=10)
        nx.draw_networkx_nodes(G, pos, self.urls, node_size=5800, node_color='gainsboro')
        nx.draw_networkx_labels(G, pos, urllabels, font_size=10)
        nx.draw_networkx_nodes(G, pos, self.docs, node_size=5800, node_color='lightblue')
        nx.draw_networkx_labels(G, pos, doclabels, font_size=12)
       
        #nx.draw_networkx_nodes(G, pos, self.opperation, node_size=5800, node_color='lightblue')
        #nx.draw_networkx_labels(G, pos, doclabels, font_size=12)
    
       
       
        nx.draw_networkx_edges(G, pos)
        
        edge_labels = {(i, k): j for i, j, k in self.clean_triples}
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=10)
        
  
      #  for x in mydict.keys():
         #   g.add_node(#self
        #            mydict[x]["operating_system"],rank=10)
            
           #print(mydict[x]['operating_system'])         
           
        plt.axis('off')
        plt.axis('square')
        plt.savefig(name)
        
      
        print("NETWORK SIZE")
        print("============")
        print("The network has {} nodes and {} edges".format(G.number_of_nodes(), G.number_of_edges()))
        print()
        
        print("DENSITY")
        print("============")
        print("The network density is {}".format(nx.density(G)))
        print()
                   

       
        
if __name__ == "__main__":

        author = Factory.new_document('shared.party')
        author.name = "Binaya Aryal"
        for p in mydict:
            computer = make_hpc(mydict[p], author)
            v = Viewer(computer)
            v.view_nx(p,f'{p}.pdf')
            
       
        #path = input("Select the path")
        #rg = RDFGraph()
        #rg.parse(path, format='json-ld')
        #print("rdflib Graph loaded successfully with {} triples".format(len(rg)))
        #G = rdflib_to_networkx_graph(rg)
        #print("networkx Graph loaded successfully with length {}".format(len(G)))  
        #print("Visualizing the graph:")
        #plt.plot()
        #nx.draw(G, with_labels=True, font_weight='bold')    
        
        
            #g is the rdflib graph 
            #https://rdflib.readthedocs.io/en/stable/plugin_serializers.html
        # v.ts.g.serialize(destination=f"{p}.xml", format='turtle')
        v.ts.g.serialize(destination=f"{p}.json", format='json-ld')
                        
           # pdfs = glob.glob('/Users/surfl/Desktop/pyosl/*.pdf')
            #new_merged_pdf = '/Users/surfl/Desktop/pyosl/allcomputerrdf.pdf'
           
            #merge_pdfs = PyPDF2.PdfFileMerger()

            #for pdf in natsorted(pdfs):
             #   merge_pdfs.append(open(pdf,'rb'))

            #merge_pdfs.write(open(new_merged_pdf, 'wb'))