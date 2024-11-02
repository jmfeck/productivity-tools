# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: jfeck
"""

import os
import pandas as pd


data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.getcwd()
path_project = os.path.dirname(path_script)
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

# initializing empty file paths list 
file_params = [] 
#yyyymmddhhnnss
#20240604131005

inc_file_path = os.path.join(path_incoming, "gbu_sap_uploader.xlsx")
out_file_path = os.path.join(path_outgoing, "gbu_sap_uploader_single_table.xlsx")
inc_sheet_name = 'gbu_arch_sap_uploader'

df = pd.read_excel(inc_file_path, sheet_name=inc_sheet_name)


#export to excel
#print(file_with_no_ext + ": exporting to excel")
df.to_excel(out_file_path, index=False)
