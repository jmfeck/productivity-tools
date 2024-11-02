# -*- coding: utf-8 -*-
"""
@author: jmfeck
"""

import configparser
import sys
import pandas_gbq as pdbq
import pandas as pd
import os

###############################################################################################################
# Config file reader
###############################################################################################################
config = configparser.RawConfigParser()
conn_config_file_path = sys.argv[1]
print(conn_config_file_path)
config.read(conn_config_file_path)

###############################################################################################################
# Functions
###############################################################################################################
def get_config_item(dict_item, var):
    config_keyvals = dict(config.items(dict_item))
    val = config_keyvals[var]
    print('INFO: ' + var + ' : ' + val)
    if not var:
        raise Exception('ERROR: ' + var + " cannot be an empty string")
    return val
       
###############################################################################################################
# Get config values
###############################################################################################################
# Get config values file_properties

#bigquery connection
project_id = get_config_item('bq_param', 'project_id')
dataset = get_config_item('bq_param', 'dataset')
tablename = get_config_item('bq_param', 'tablename')
table_id = dataset + '.' + tablename

#project parameters
data_incoming_foldername = get_config_item('project_param', 'data_incoming_foldername')

#project parameters
file_relative_path = get_config_item('file_param', 'file_relative_path')
file_radc = get_config_item('file_param', 'file_radcname')
file_ext = get_config_item('file_param', 'file_ext')
sheet_name = get_config_item('file_param', 'sheet_name')

##########################main##########################
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_file = os.path.join(data_incoming_foldername, file_relative_path, file_radc + file_ext)


df = pd.read_excel(path_file, sheet_name=sheet_name)
pdbq.to_gbq(df, table_id, project_id=project_id)
