# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:23:22 2020

@author: WCY8676
"""

import pandas as pd
import os
import requests
import sys

###############################################################################################################
# Functions
###############################################################################################################



###############################################################################################################
# Config file reader
###############################################################################################################
inc_filename = sys.argv[1]
partition_selector = sys.argv[2]

print(inc_filename)
print(partition_selector)

##########################main##########################

inc_sheetname = inc_filename.split('.')[0]

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

list_links_path = os.path.join(path_incoming, inc_filename)
print(list_links_path)
print(inc_sheetname)
df = pd.read_excel(list_links_path, sheet_name=inc_sheetname, dtype=str)
df = df[df['partition'] == partition_selector] 

for index, row in df.iterrows():
    file_prefix = row['prefix']
    file_sufix = row['sufix']
    file_url = row['url']
    file_name = row['url'].split('/')[-1]
    file_out_path = os.path.join(path_outgoing, file_prefix + '__' + file_sufix + '__' + file_name)
    
    print(file_prefix)
    print(file_sufix)
    print(file_url)
    
    r = requests.get(file_url)
    f = open(file_out_path, 'wb')
    f.write(r.content)