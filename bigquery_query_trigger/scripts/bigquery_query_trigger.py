# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 18:23:22 2020

@author: WCY8676
"""

import configparser
import sys
from google.cloud import bigquery
import os

###############################################################################################################
# Config file reader
###############################################################################################################

config = configparser.RawConfigParser()
conn_config_file_path = sys.argv[1]
print(conn_config_file_path)
config.read(conn_config_file_path)

###############################################################################################################
# Query file reader
###############################################################################################################
sql_file_path = sys.argv[2]
sql_file = open(sql_file_path, 'r')
sql_queries = sql_file.read()
sql_file.close()
sql_queries_list = sql_queries.split(';')
print(sql_queries_list[0])

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

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_file = os.path.join(path_project, conn_config_file_path)

##########################main##########################

client = bigquery.Client(project=project_id)
for sql_query in sql_queries_list:
	print(sql_query)
	query_job = client.query_and_wait(sql_query, location="EU")
	print("Got {} rows.".format(query_job.total_rows))
