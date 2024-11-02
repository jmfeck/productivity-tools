# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: WCY8676
"""

import os
import logging
import pandas as pd

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

file_dtypes = 'str'

# initializing empty file paths list 
file_params = [] 


# crawling through directory and subdirectories 
for root, directories, files in os.walk(path_incoming): 
    for filename in files: 
        # join the two strings in order to form the full filepath. 
        file_with_no_ext = filename.split('.')[0]
        inc_file_path = os.path.join(root, filename) 
        out_file_path =  os.path.join(path_outgoing, file_with_no_ext + '.xlsx') 
        file_params.append([inc_file_path, out_file_path, filename, file_with_no_ext]) 

for file_param in file_params:
    inc_file_path = file_param[0]
    out_file_path = file_param[1]
    filename = file_param[2]
    file_with_no_ext = file_param[3]

    if not(inc_file_path.endswith(".xls")):
    	print(file_with_no_ext + ": not xls file")
    	continue
    
    print(file_with_no_ext + ": starting")
    
    #reading excel
    print(file_with_no_ext + ": importing data")

    df = pd.read_excel(inc_file_path, sheet_name=file_with_no_ext, dtype=file_dtypes)

    #export to excel
    print(file_with_no_ext + ": exporting to excel")
    dfstp0.to_excel(out_file_path, index=False)
    print(file_with_no_ext + ": finished")