# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:23:22 2020

@author: WCY8676
"""

import configparser
import sys
import snowflake.connector
import pandas as pd
import pandas_gbq as pdbq
import os
import re
import json

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
table_id = '.'.join([project_id, dataset, tablename])

#project parameters
data_outgoing_foldername = get_config_item('project_param', 'data_outgoing_foldername')

#file parameters
file_relative_path = get_config_item('file_param', 'file_relative_path')
file_radc = get_config_item('file_param', 'file_radcname')
file_ext = get_config_item('file_param', 'file_ext')
file_sheetname = get_config_item('file_param', 'sheet_name')

##########################main##########################
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_file = os.path.join(data_outgoing_foldername, file_relative_path, file_radc + file_ext)

print("read table")
sql = f"SELECT * FROM {table_id}"
print(sql)
df = pdbq.read_gbq(sql, project_id=project_id)


#print(df.dtypes)
#df = df.astype({'ID':'string'})
#df['ID'] = df['ID'].str.decode('utf-8')
#print(df.dtypes)

print("export table")
if file_ext == ".parquet":
    df.to_parquet(path=path_file, index = False)
if file_ext == ".csv":
    df.to_csv(path_or_buf=path_file, index = False)
if file_ext == ".xlsx":
    df.to_excel(path_file, sheet_name = file_sheetname, index = False)
