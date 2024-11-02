# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import configparser
import sys
from google.cloud import bigquery
import os

###############################################################################################################
# Config file reader
###############################################################################################################

config = configparser.RawConfigParser()
conn_config_file_path = sys.argv[1]
print(f"Loading configuration from: {conn_config_file_path}")
config.read(conn_config_file_path)

###############################################################################################################
# Query file reader
###############################################################################################################
sql_file_path = sys.argv[2]
print(f"Executing queries from: {sql_file_path}")

with open(sql_file_path, 'r') as sql_file:
    sql_queries = sql_file.read()

sql_queries_list = [query.strip() for query in sql_queries.split(';') if query.strip()]

###############################################################################################################
# Functions
###############################################################################################################
def get_config_item(dict_item, var):
    config_keyvals = dict(config.items(dict_item))
    val = config_keyvals[var]
    print('INFO: ' + var + ' : ' + val)
    if not val:
        raise Exception(f"ERROR: {var} cannot be an empty string")
    return val

###############################################################################################################
# Get config values
###############################################################################################################
# BigQuery connection
project_id = get_config_item('bq_param', 'project_id')
dataset = get_config_item('bq_param', 'dataset')
tablename = get_config_item('bq_param', 'tablename')
table_id = f"{project_id}.{dataset}.{tablename}"

# Project parameters
data_outgoing_foldername = get_config_item('project_param', 'data_outgoing_foldername')

# File parameters
file_relative_path = get_config_item('file_param', 'file_relative_path')
file_radc = get_config_item('file_param', 'file_radcname')
file_ext = get_config_item('file_param', 'file_ext')
file_sheetname = get_config_item('file_param', 'sheet_name')

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_file = os.path.join(path_project, conn_config_file_path)

###############################################################################################################
# Main Process
###############################################################################################################

client = bigquery.Client(project=project_id)
for sql_query in sql_queries_list:
    if sql_query:
        print(f"Executing query:\n{sql_query}")
        query_job = client.query(sql_query, location="EU")
        results = query_job.result()  # Wait for job to complete
        print(f"Query executed successfully. Got {results.total_rows} rows.")
