# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import os
import pandas as pd
import logging


data_incoming_foldername = 'input'
data_outgoing_foldername = 'output'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_input = os.path.join(path_project, data_incoming_foldername)
path_output = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

logging.basicConfig(filename=path_log,level=logging.DEBUG)

inc_sep = ','
inc_dec = '.'

out_sep = ';'
out_dec = '.'

# initializing empty file paths list 
file_params = [] 
  
# crawling through directory and subdirectories 
for root, directories, files in os.walk(path_input): 
    for filename in files: 
        # join the two strings in order to form the full filepath. 
        file_with_no_ext = filename.split('.')[0]
        inc_file_path = os.path.join(root, filename) 
        out_file_path =  os.path.join(path_output, file_with_no_ext + '.csv') 
        file_params.append([inc_file_path, out_file_path, filename, file_with_no_ext]) 

for file_param in file_params:
    inc_file_path = file_param[0]
    out_file_path = file_param[1]
    filename = file_param[2]
    file_with_no_ext = file_param[3]
    
    logging.info(file_with_no_ext + ": starting")
    
    #reading excel
    logging.info(file_with_no_ext + ": reading csv to be converted")
    dfstp0 = pd.read_csv(inc_file_path, dtype=str, sep=inc_sep, decimal=inc_dec)

    #export to excel
    logging.info(file_with_no_ext + ": exporting to csv with semicolon format")
    dfstp0.to_csv(out_file_path, index=False, sep=out_sep, decimal=out_dec)
    logging.info(file_with_no_ext + ": finished")