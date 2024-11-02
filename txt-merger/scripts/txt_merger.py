# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import os
import pandas as pd
import logging

dict_info = {
        "row_index" : [],
        "row_content" : [],
        "filename" : []
        }

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

logging.basicConfig(filename=path_log,level=logging.DEBUG)

# initializing empty file paths list 
file_params = [] 
  
# crawling through directory and subdirectories 
for root, directories, files in os.walk(path_incoming): 
    for filename in files: 
        # join the two strings in order to form the full filepath. 
        file_with_no_ext = filename.split('.')[0]
        inc_file_path = os.path.join(root, filename) 
        file_params.append([inc_file_path, filename, file_with_no_ext]) 

for file_param in file_params:  
    inc_file_path = file_param[0]
    filename = file_param[1]
    file_with_no_ext = file_param[2]
    
    logging.info(file_with_no_ext + ": starting")
    
    #reading
    file = open(inc_file_path, 'r')
    lines = file.read().splitlines()
    file.close()
    
    i = 1
    for line in lines:
        if not line:
            continue
        dict_info["row_index"].append(i)
        dict_info["row_content"].append(line)
        dict_info["filename"].append(file_with_no_ext)
        i = i + 1

df_info = pd.DataFrame(dict_info)
df_info.to_excel(os.path.join(path_outgoing, 'files_info' + '.xlsx') , sheet_name='files_info', index=False, engine='xlsxwriter')
