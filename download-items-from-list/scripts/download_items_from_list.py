# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import pandas as pd
import os
import requests
import logging

###############################################################################################################
# Config file reader
###############################################################################################################

inc_filename = 'list_links.xlsx'
inc_sheetname = inc_filename.split('.')[0]

input_foldername = 'input'
output_foldername = 'output'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_input = os.path.join(path_project, input_foldername)
path_output = os.path.join(path_project, output_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

logging.basicConfig(filename=path_log,level=logging.DEBUG)

logging.info("Starting downloads...")
list_links_path = os.path.join(path_input, inc_filename)
df = pd.read_excel(list_links_path, sheet_name=inc_sheetname, dtype=str)

for index, row in df.iterrows():
    file_url = row['link_url']
    file_name = row['link_url'].split('/')[-1]
    file_out_path = os.path.join(path_output, file_name)

    logging.info(file_name + ": Starting download")
    r = requests.get(file_url)
    f = open(file_out_path, 'wb')
    
    f.write(r.content)
    logging.info(file_name + ": Download sucessful")