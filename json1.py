#!/usr/bin/python
#coding=utf-8
import pandas as pd
import re
import os
import sys
import operator
import sqlite3
import random
import string
from tabulate import tabulate
import mysql.connector
import json

#mydb = mysql.connector.connect(
# host="localhost".
# user="root",
# passwd="Test@123"
#)


sq = sqlite3.connect("computers.db")
sqcur = sq.cursor()


#with open('data.txt') as json_file:
#    data = json.load(json_file)


path = 'jsonFiles'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if '.json' in file:
            files.append(os.path.join(r, file))

for f in files:
    with open(f) as json_file:
        data = json.load(json_file)
        r = json.dumps(data)
        v = json.loads(r)
        
        name_of_computer = v['name']
        name_of_institute = v['institution']['name']
        name_of_vendor = v['vendor']['name']
        peak_performance = 1
        linpack_performance = 2
        
        if 'peak_performance' not in v:
            peak_performance = None
        else:
            peak_performance = v['peak_performance']['value']
        if 'linpack_performance' not in v:
            linpack_performance = None
        else:
            linpack_performance = v['linpack_performance']['value']

        if 'operating_system' not in v:
            operating_system = None
        else:
            operating_system = v['operating_system']
        if 'peak_performance' not in v:
            peak_performance_units = None
        else:
            peak_performance_units = v['peak_performance']['units']
        if 'linpack_performance' not in v:
            linpack_performance_units = None
        else:
            linpack_performance_units = v['linpack_performance']['units']

        list_documentation = []
        storage_pools = []
        computer_pools = []
        network_cards_per_node = []
        for ele in v['online_documentation']:
            val1 = ele['linkage']
            val2 = ele['name']
            var = []
            var.append(val1)
            var.append(val2)
            list_documentation.append(var)

        for ele in v['storage_pools']:
            var = []
            if 'name' not in ele:
                var.append(None)
            else:
                var.append(ele['name'])
            if 'type' not in ele:
                var.append(None)
            else:
                var.append(ele['type'])
            if 'file_system_sizes' not in ele:
                var.append(None)
                var.append(None)
            else:
                var.append(ele['file_system_sizes'][0]['value'])
                var.append(ele['file_system_sizes'][1]['units'])
            storage_pools.append(var)

        for ele in v['compute_pools']:
            var = []
            if 'name' not in ele:
                var.append(None)
            else:
                var.append(ele['name'])

            if 'clock_cycle_concurrency' not in ele:
                var.append(None)
            else:
                var.append(ele['clock_cycle_concurrency'])

            if 'model_number' not in ele:
                var.append(None)
            else:
                var.append(ele['model_number'])

            if 'cpu_type' not in ele:
                var.append(None)
            else:
                var.append(ele['cpu_type'])

            if 'processor' not in ele:
                var.append(None)
            else:
                var.append(ele['processor'])

            if 'accelerator_type' not in ele:
                var.append(None)
            else:
                var.append(ele['accelerator_type'])

            if 'accelerators_per_node' not in ele:
                var.append(None)
            else:
                var.append(ele['accelerators_per_node'])

            if 'clock_speed' not in ele:
                var.append(None)
            else:
                var.append(ele['clock_speed']['value'])

            if 'description' not in ele:
                var.append(None)
            else:
                var.append(ele['description'])

            if 'memory_per_node' not in ele:
                var.append(None)
            else:
                var.append(ele['memory_per_node']['value'])

            if 'number_of_nodes' not in ele:
                var.append(None)
            else:
                var.append(ele['number_of_nodes'])

            if 'compute_cores_per_node' not in ele:
                var.append(None)
            else:
                var.append(ele['compute_cores_per_node'])

            if 'clock_speed' not in ele:
                var.append(None)
            else:
                var.append(ele['clock_speed']['units'])

            if 'memory_per_node' not in ele:
                var.append(None)
            else:
                var.append(ele['memory_per_node']['units'])

            if 'network_cards_per_node' in ele:
                lis = ele['network_cards_per_node']
                for j in lis:
                    vari = []
                    vari.append(ele['name'])
                    if 'name' in j:
                        vari.append(j['name'])
                    else:
                        vari.append(None)
                    if 'bandwidth' in j:
                        vari.append(j['bandwidth']['value'])
                        vari.append(j['bandwidth']['units'])
                    else:
                        vari.append(None)
                        vari.append(None)
                    network_cards_per_node.append(vari)
            computer_pools.append(var)
        sql = "INSERT INTO computerInformation (name,institution,vendor,operating_system,peak_performance_value,linpack_performace_value, peak_performance_units,linpack_performace_units) VALUES (?, ?, ?, ?, ?, ?, ?,  ?)"
        val = (name_of_computer, name_of_institute, name_of_vendor, operating_system, peak_performance, linpack_performance,  peak_performance_units, linpack_performance_units)
        sqcur.execute(sql, val)
        sq.commit()

        for ii in range(len(list_documentation)):
            sql = "INSERT INTO online_documentation (name,linkage,Type) VALUES (?, ?, ?)"
            val = (name_of_computer, list_documentation[ii][0],  list_documentation[ii][1])
            sqcur.execute(sql, val)
            sq.commit()

        for ii in range(len(storage_pools)):
            sql = "INSERT INTO storagePools (name, type, file_system_sizes_value, name_storage_pool, file_system_sizes_units) VALUES (?, ?, ?, ?, ?)"
            val = (name_of_computer, storage_pools[ii][1],  storage_pools[ii][2], storage_pools[ii][0], storage_pools[ii][3])
            sqcur.execute(sql, val)
            sq.commit()

        for ii in range(len(computer_pools)):
            sql = "INSERT INTO computerPools (name, name_computer_pools, accelerator_type, accelerator_per_node, cpu_type, computer_cores_per_node, clock_cycle_concurrency,clock_speed_value,description,memory_per_node_value,number_of_nodes,model_number,processor, clock_speed_units, memory_per_node_units) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (name_of_computer, computer_pools[ii][0],  computer_pools[ii][5], computer_pools[ii][6], computer_pools[ii][3], computer_pools[ii][11], computer_pools[ii][1], computer_pools[ii][7], computer_pools[ii][8], computer_pools[ii][9], computer_pools[ii][10], computer_pools[ii][2], computer_pools[ii][4], computer_pools[ii][12], computer_pools[ii][13])
            sqcur.execute(sql, val)
            sq.commit()

        for ii in range(len(network_cards_per_node)):
            sql = "INSERT INTO networkCardsPerNode (name, name_of_compute_pools, name_of_network,  bandwidth_value, bandwidth_units) VALUES (?, ?, ?, ?, ?)"
            val = (name_of_computer, network_cards_per_node[ii][0],  network_cards_per_node[ii][1], network_cards_per_node[ii][2], network_cards_per_node[ii][3])
            sqcur.execute(sql, val)

sq.commit()
