#from pyosl.tools import numeric_value
import json
mydict = {'Summit': {

    'name': 'Summit',
     # use dictionaries for sub-class information to separate information you want to go into a subclass
    'institution': {'name': 'U.S Department of Energy'},
    'vendor': {'name': 'IBM'},

    'operating_system': '(RHEL 7.4)',
    'software' : 'sad' , 
    # we could use the same notation for the numeric_values, which would be cleaner
    'peak_performance': {'value' : 220.00, 'units' : 'PF' },
    'linpack_performance': {'value' : 454.00, 'units' : 'PF' },

    # could be many compute pools or storage pools, so we need a special notation for them using a list
    # (we do the same thing for any list).

    'compute_pools': [
        {'name': 'Standard Nodes',

         'clock_cycle_concurrency': 3,

         'model_number': 'AC922',
         'cpu_type': 'Power9',
         'accelerator_type' : 'GPU Type, NVIDIA Volta V100',
         'accelerators_per_node': 6 ,
         'clock_speed': {'value' : 200.00, 'units' : 'PF' },
         'description': 'Two IBM CPUs per node and 6 NVIDIA accelerators per node',
         'memory_per_node': {'value' : 512.00, 'units' : 'GB DDR4' },
         'number_of_nodes': 4608,
         'network_cards_per_node': [
             {'name': 'Mellanox Infiniband EDR', 'bandwidth': {'value' : 200.00, 'units' : 'GB/s' },},
         ],
         },
    ],

    'storage_pools': [
        {'name':'Alpine', 'type':'GPFS', 'file_system_sizes': [{'value' : 250.00}, {'units' : 'PB'}] },   
        # didn't include the TDS, as most sites don't give TDS information.
],

    'online_documentation': [
        {'linkage': 'https://www.olcf.ornl.gov/olcf-resources/compute-systems/summit/',
         'name': 'website'},
    ],
    },


'Sierra': {

    'name': 'Sierra',
    'institution': {'name': 'National Nuclear Security Adminstration'},
    'vendor': {'name': 'IBM'},
    'operating_system': '(Linux RHEL) ',
   'peak_performance': {'value' : 125.00, 'units' : 'PF' },
    'linpack_performance': {'value' : 200.00, 'units' : 'PF' },
    'compute_pools': [
        {'name': 'Standard Nodes',
         'model_number': 'ATS-2',
         'cpu_type': 'Power9',
         'accelerator_type' : 'Nvidia V100 Volta',
         'accelerators_per_node': 4 ,
         'clock_cycle_concurrency': 3,
         'compute_cores_per_node' : 44,
         'clock_speed': {'value' : 3.1, 'units' : 'GHZ' },
         'description': 'Sierra combines two types of processor chips—IBM’s Power 9 processors and NVIDIA’s Volta graphics processing units (GPUs)',
         'memory_per_node': {'value' : 256.00, 'units' : 'GB DDR4' },
         'number_of_nodes': 4320,
         'network_cards_per_node': [
             {'name': 'Mellanox Infiniband EDR', 'bandwidth': {'value' : 200.00, 'units' : 'GB/s' }}
         ],
         },
    ],

    'storage_pools': [
        {'name':'IBM Spectrum Scale SCF ZONE', 'type':'GPFS', 'file_system_sizes': [{'value' : 140.00}, {'units' : 'PB'} ]},
     ],
    'online_documentation': [
        {'linkage': 'https://computing.llnl.gov/computers/sierra',
         'name': 'website'},
    ],

    },

'SunwayTaihuLight': {
    'name': 'SunwayTaihuLight',
    'institution': {'name': 'National Supercomputing Center in Wuxi'},
    'vendor': {'name': 'NRCPC'},
    'operating_system': '(Sunway RaiseOS 2.0.5 (based on Linux)) ',
'peak_performance': {'value' : 125.44, 'units' : 'PF' },
    'linpack_performance': {'value' : 93.01, 'units' : 'PF' },
    'compute_pools': [
        {'name': 'Standard Nodes',
         'cpu_type': 'Sunway SW26010 260C',
         'accelerator_type' : 'NVIDIA GPU or Intel Xeon Phi',
         #'accelerators_per_node': '10B' ,
         #'clock_cycle_concurrency': 3,
         'compute_cores_per_node' : 260,
         'clock_speed': {'value' : 93.00, 'units' : 'Trillion/sec' },
         'description': 'Sierra combines two types of processor chips—IBM’s Power 9 processors and NVIDIA’s Volta graphics processing units (GPUs)',
         'memory_per_node': {'value' : 32.00, 'units' : 'GB' },
         'number_of_nodes': 40960,
         'network_cards_per_node': [
             {'name': 'Sunway Network', 'bandwidth':  {'value' : 70.00, 'units' : 'TB' }},
         ],
         },
    ],

    'storage_pools': [
                { 'name':'Iccefish Storage System', 'type':' Lustre', 'file_system_sizes':  [{'value' : 10.00}, {'units' : 'PB'}] },
         
      
    ],

    'online_documentation': [
        {'linkage': 'http://www.netlib.org/utk/people/JackDongarra/PAPERS/sunway-report-2016.pdf',
         'name': 'website'},
    ],

   },


'Tianhe-2A': {
    'name': 'Tianhe-2A',
    'institution': {'name': 'National Supercomputing Center in Guangzhou'},
    'vendor': {'name': 'NUDT'},
    'operating_system': '(Linux (Kylin)) ',
    'peak_performance':  {'value' : 94.97, 'units' : 'PF' },
    'linpack_performance':  {'value' : 33.86, 'units' : 'PF' },
    'compute_pools': [
        {'name': 'Standard Nodes',
         'cpu_type': 'Intel Xeon Ivy Bridge plus Matrix-2000 accelerator',
         'accelerator_type' : 'Matrix-2000',
         'accelerators_per_node': 32 ,
         'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 280,
         #'processor' : ' Xeon E5–2692 v2, Matrix-2000',
         'clock_speed':  {'value' : 33.86, 'units' : 'GB' },
         'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         'memory_per_node':  {'value' : 192.00, 'units' : 'GB' }, 
         'number_of_nodes': 17792,
         'network_cards_per_node': [
            {'name': 'TH Express 2 network', 'bandwidth':  {'value' : 16.00, 'units' : 'GB' }},
         ],
         },

    ],

    'storage_pools': [
        {'name':'Parallel File System', 'type':' Lustre', 'file_system_sizes':  [{'value' : 19.00}, {'units' : 'PB'}]
         },
           ],

    'online_documentation': [
        {'linkage': 'https://www.icl.utk.edu/files/publications/2017/icl-utk-970-2017.pdf',
         'name': 'website'},
    ],
            },
            
'Frontera': {

    'name': 'Frontera',
    'institution': {'name': 'Texas Advanced Computing Center'},
    'vendor': {'name': 'Dell EMC'},

    'operating_system': '(Linux (CentOS)) ',


    'peak_performance':  {'value' : 38.80, 'units' : 'PF' },
    'linpack_performance':  {'value' : 23.50, 'units' : 'PF' },


    'compute_pools': [
        {'name': 'Standard Nodes',
          'accelerator_type' : '360 NVIDIA Quadro RTX 5000 GPUs',
             'accelerators_per_node': 4 ,

         'cpu_type': 'Intel(R) Xeon(R) CPU E5-2620 v4 ',
         'compute_cores_per_node' : 56,


         'clock_cycle_concurrency': 2,

         'clock_speed':  {'value' : 2.7, 'units' : 'GHz' },
         'description': 'powerful resource for data science and machine learning applications',
         'memory_per_node': {'value' : 256., 'units' : 'GB' },
         'number_of_nodes': 17609,

         'network_cards_per_node': [
             {'name': 'Mellanox Infiniband EDR', 'bandwidth':  {'value' : 200.00, 'units' : 'GB' }},
         ],
         },
    ],

    'storage_pools': [
        {'name':'Fast Scratch', 'type':'NVMe', 'file_system_sizes':  [{'value' : 4.00}, {'units' : 'PB'} ] 
                                                                     },
    {'name':'Scratch/Work', 'type':'Disk ', 'file_system_sizes':  [{'value' : 50.00}, {'units' : 'PB'}] },
       
    ],


    'online_documentation': [
        {'linkage': 'https://www.tacc.utexas.edu/systems/frontera',
         'name': 'website'},
    ],

    },

    'PizDaint':

        { 'name': 'PizDaint',
    'institution': {'name': 'Swiss National Supercomputing Centre'},
    'vendor': {'name': 'CRAY'},

    'operating_system': '(Linux CLE) ',


    'peak_performance':  {'value' : 25.00, 'units' : 'PF' },
    'linpack_performance':  {'value' : 19.3, 'units' : 'PF' },


    'compute_pools': [
        {'name': 'Standard Nodes',
         'model_number': 'CRAY XC30',
         'cpu_type': 'Intel® Xeon® E5- 2690 v3',
         'accelerator_type' : 'NVIDIA® Tesla® P100',
         'accelerators_per_node': 1 ,
         #'clock_cycle_concurrency': 3,
         'compute_cores_per_node' : 12,
         
         'clock_speed':  {'value' : 25.32, 'units' : 'PF' } ,
         'memory_per_node':  {'value' : 32.00, 'units' : 'GB DDR3-1600' },
         'number_of_nodes': 5704,
                'network_cards_per_node': [
             {'name': 'Cray Aries'},
         ],
         },
    ],

  'storage_pools': [

        {'name':'Home Filsystem',  'type' : 'GPFS',  'file_system_sizes':  [{'value' : 160.00}, {'units' : 'TB'} ]
         },
    {'name':'Work File System',  'type' : 'GPFS', 'file_system_sizes':  [{'value' : 6.3}, {'units' : 'PB' }]
         },
             {'name':'Scratch File System ',  'type' : 'Lustre',  'file_system_sizes':  [{'value' : 8.8}, {'units' : 'PB' }],
         },

          ],

    'online_documentation': [
        {'linkage': 'https://www.cscs.ch/computers/piz-daint/',
         'name': 'website'},
    ],
            },



      'Trinity': {
    'name': 'Trinity',
    'institution': {'name': 'Los Alamos National Laboratory'},
    'vendor': {'name': 'CRAY'},
    'operating_system': 'Linux (CLE) ',


    'peak_performance':  {'value' : 41.5, 'units' : 'PF' },
    'linpack_performance':  {'value' : 20.2, 'units' : 'PF' },


    'compute_pools': [

        {'name': 'Standard Nodes',
         'cpu_type': 'Xeon E5-2600 ',

         'accelerator_type' : 'Nvidia Telsa K40, X86',
         'model_number' :'Cray XC40',
         #'accelerators_per_node': 32 ,
         #'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 32,
           'clock_speed':  {'value' : 33.86, 'units' : 'PF' },
         #'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         'memory_per_node':  {'value' : 1.7, 'units' : 'TBps' },
         'number_of_nodes': 19420,
         'network_cards_per_node': [
            {'name': 'Cray Aries'},
         ],
         },

    ],

    'storage_pools': [

        {'name':'Sonexion', 'type':' Lustre', 'file_system_sizes':  [{'value' : 78.0}, {'units' : 'PB'} ]
         },
    {'name':'Memory', 'type':' DRAM', 'file_system_sizes':  [{'value' : 2.0}, {'units' : 'PB' }]
         },
             {'name':'Burst Buffer', 'file_system_sizes':  [{'value' : 3.78}, {'units' : 'PB' }]
         },
                {'name':'MarFS Filesystem', 'type':' POISX','file_system_sizes': [{'value' : 100.0}, {'units' : 'PB' }]
         },
              {'name':'Archive','type':' HPSS', 'file_system_sizes':  [{'value' : 100.0}, {'units' : 'PB' }]
         },
        # didn't include the TDS, as most sites don't give TDS information.
    ],

    'online_documentation': [
        {'linkage': 'https://lanl.gov/projects/trinity/',
         'name': 'website'},
    ],
            },


      'AIBridgingCloudInfrastructure': {
    'name': 'AIBridgingCloudInfrastructure',
    'institution': {'name': 'National Institute of Advanced Industrial Science and Technology'},
    'vendor': {'name': 'Fujitsu'},
    'operating_system': 'Linux ',


    'peak_performance':  {'value' : 37.2, 'units' : 'PF' },

    'linpack_performance': {'value' : 19880., 'units' : 'TF' },


    'compute_pools': [

        {'name': 'Standard Nodes',
         'cpu_type': ' IXeon Gold 6148 20C 2.4GHz ',
         'accelerator_type' : 'NVIDIA Tesla V100',
         #'accelerators_per_node': 32 ,
         #'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 4,
         #'processor' : ' Xeon E5–2692 v2, Matrix-2000',
         #clock_speed': 33.86,
         #'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         #'memory_per_node': 1.7,
         'number_of_nodes': 1088,
         'network_cards_per_node': [
            {'name': 'Mellanox Infiniband EDR'},
         ],
         },

    ],

    'storage_pools': [

        {'name':'Home Area', 'type':' Lustre', 'file_system_sizes': [{'value' : 1.}, {'units' : 'PF' }]
         },
    {'name':'Group Area 1', 'type':' GPPS', 'file_system_sizes': [{'value' : 6.6}, {'units' : 'PF' }]
         },
             {'name':'Group Area 2','type':' GPPS',  'file_system_sizes': [{'value' : 6.6}, {'units' : 'PF' }]
         },
                {'name':'Application Area', 'type':'GPPS','file_system_sizes': [{'value' : 335.}, {'units' : 'TB' }]
         },
              {'name':'Local scratch area for intaractive node','type':' XPS', 'file_system_sizes': [{'value' : 12.}, {'units' : 'TB' }]
         },
        {'name':'Local scratch area for compute node','type':' XFS', 'file_system_sizes':  [{'value' : 1.5}, {'units' : 'TB' }]
         },
          ],


    'online_documentation': [
        {'linkage': 'https://www.hpci-office.jp/pages/e_aist_2019-1',
         'name': 'website'},
    ],
            },



    'SuperMUC-NG': {
    'name': 'SuperMUC-NG',
    'institution': {'name': 'Leibniz Supercomputing Centre'},
    'vendor': {'name': 'Lenovo'},
    'operating_system': 'Suse Linux (SLES) ',


    'peak_performance':  {'value' : 26.7, 'units' : 'PF' },
    'linpack_performance': {'value' : 20.4, 'units' : 'PF' },

    'compute_pools': [

        {'name': 'Thin Compute Nodes',
         'cpu_type': ' Intel Skylake Xeon Platinum 8174',

         'accelerator_type' : 'NVIDIA Tesla V100 SXM2 ×4',
         #'accelerators_per_node': 32 ,
         #'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 48,

         #clock_speed': 33.86,
         #'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         'memory_per_node': {'value' : 96., 'units' : 'GB' },
         'number_of_nodes': 6336,
         'network_cards_per_node': [
           {'name': 'Intel OmniPath Architecture '},
        ],

        #interconnect=  Fat tree within island(786 nodes)pruned treebetweenislands
         },


         {'name': 'Fat Compute Nodes',
         'cpu_type': ' Intel Skylake Xeon Platinum 8174',
         'accelerator_type' : 'NVIDIA Tesla V100 SXM2 ×4',
         #'accelerators_per_node': 32 ,
         #'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 48,

         #clock_speed': 33.86,
         #'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         'memory_per_node': {'value' : 768., 'units' : 'GB' },
         'number_of_nodes': 144,

         #'network_cards_per_node': [
           # {'name': 'Cray Aries'},
        # ],
         },


    ],
       'storage_pools': [

        {'name':'Home Filsystem',  'type' : 'GPFS',  'file_system_sizes': [{'value' : 265.}, {'units' : 'TB' }]
         },
    {'name':'Work File System',  'type' : 'GPFS', 'file_system_sizes':  [{'value' : 33.}, {'units' : 'TB' }]
         },
             {'name':'Scratch File System ',  'type' : 'GPFS',  'file_system_sizes':  [{'value' : 17.}, {'units' : 'TB' }]
         },

          ],

    'online_documentation': [
        {'linkage': 'https://doku.lrz.de/display/PUBLIC/SuperMUC-NG',
         'name': 'website'},
    ],

            },


'Lassen': {
    'name': 'Lassen',
    'institution': {'name': 'Lawrence Livermore National Laboratory'},
    'vendor': {'name': 'IBM'},
    'operating_system': '	Red Hat Enterprise Linux ',


    'peak_performance': {'value' : 23.5, 'units' : 'PF' },
    'linpack_performance':  {'value' : 18.2, 'units' : 'PF' },

   'compute_pools': [
        {'name': 'Standard Nodes',
         'cpu_type': ' IBM Power9',

         'accelerator_type' : 'NVIDIA Tesla V100 SXM2 ×4',
         'accelerators_per_node': 4 ,
         #'clock_cycle_concurrency': 17,
         'compute_cores_per_node' : 44,

         'clock_speed':  {'value' : 3.5, 'units' : 'GHZ' },
         #'description': 'Developed by China National University of Defense Technology, retains its position as the worlds No. 1 system with a performance',
         'memory_per_node':  {'value' : 320., 'units' : 'GB' },
         'number_of_nodes': 684,

         'network_cards_per_node': [
           {'name': 'InfiniBand EDR '},
        ],
                 },
         ],


   'storage_pools': [

        {'name':'CZ Filsystem',  'type' : 'GPFS',  'file_system_sizes':  [{'value' : 24.}, {'units' : 'PB' }]
         }
   
          ],

'online_documentation': [
        {'linkage': 'https://computing.llnl.gov/computers/lassen',
         'name': 'website'},
    ],

    },
    }


r = json.dumps(mydict)
loaded_r = json.loads(r)
loaded_r['Summit'] #Output 3.5
print (type(r)) #Output str
print (type(loaded_r)) #Output dict

for k,v in loaded_r.items():
    fileName = "jsonFiles/" + k + ".json"
    with open(fileName, 'w') as outfile:
        json.dump(v, outfile)

