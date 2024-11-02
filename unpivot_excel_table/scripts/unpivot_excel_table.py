# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: WCY8676
"""

import os
import logging
import time


def print_elapsed_time(prefix=''):
    e_time = time.time()
    if not hasattr(print_elapsed_time, 's_time'):
        print_elapsed_time.s_time = e_time
    else:
        print(f'{prefix} elapsed time: {e_time - print_elapsed_time.s_time:.2f} sec')
        print_elapsed_time.s_time = e_time

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.getcwd()
path_project = os.path.dirname(path_script)
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

file_dtypes = 'str'
separator = ','
dec = '.'

# initializing empty file paths list 
file_params = [] 

print_elapsed_time()

if __name__ == "__main__":
    import pandas as pd
    # crawling through directory and subdirectories 
    for root, directories, files in os.walk(path_incoming): 
        for filename in files: 
            # join the two strings in order to form the full filepath. 
            file_with_no_ext = filename.split('.')[0]
            inc_file_path = os.path.join(root, filename) 
            out_file_path =  os.path.join(path_outgoing, file_with_no_ext + '.csv') 
            file_params.append([inc_file_path, out_file_path, filename, file_with_no_ext]) 
    print_elapsed_time('after maping incoming file')
    for file_param in file_params:
        inc_file_path = file_param[0]
        out_file_path = file_param[1]
        filename = file_param[2]
        file_with_no_ext = file_param[3]
        
        print(file_with_no_ext + ": starting")
        
        #reading excel
        print(file_with_no_ext + ": importing data")

        eng = None
        dfstp0 = pd.read_excel(inc_file_path, sheet_name=file_with_no_ext, dtype=file_dtypes, engine=eng)
        print_elapsed_time(file_with_no_ext + ": after ingesting file to pandas")

        eng = "openpyxl"
        dfstp0 = pd.read_excel(inc_file_path, sheet_name=file_with_no_ext, dtype=file_dtypes, engine=eng)
        print_elapsed_time(file_with_no_ext + ": after ingesting file to pandas " + eng)

        #export to excel
        print(file_with_no_ext + ": exporting to excel")
        dfstp0.to_csv(out_file_path, index=False, sep=separator, decimal=dec)
        print_elapsed_time(file_with_no_ext + ": after exporting file to csv")
        print(file_with_no_ext + ": finished")