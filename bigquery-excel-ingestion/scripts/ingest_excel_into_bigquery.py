# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import sys
import pandas as pd
import pandas_gbq as pdbq
import os
import yaml

###############################################################################################################
# Config file reader
###############################################################################################################
def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    print(f"Configuration loaded from {file_path}")
    return config

# Load the YAML configuration file
conn_config_file_path = sys.argv[1]
config = load_config(conn_config_file_path)

###############################################################################################################
# Functions
###############################################################################################################
def get_config_item(config_section, var):
    """Retrieve a configuration item and ensure it's not empty."""
    try:
        val = config_section[var]
        print('INFO:', var, ':', val)
        if not val:
            raise ValueError(f"{var} cannot be an empty string")
        return val
    except KeyError:
        raise KeyError(f"Missing configuration for {var}")

###############################################################################################################
# Get config values
###############################################################################################################
# BigQuery connection parameters
project_id = get_config_item(config['bq_param'], 'project_id')
dataset = get_config_item(config['bq_param'], 'dataset')
tablename = get_config_item(config['bq_param'], 'tablename')
table_id = f"{dataset}.{tablename}"

# Project parameters
data_incoming_foldername = get_config_item(config['project_param'], 'input_foldername')

# File parameters
file_relative_path = get_config_item(config['file_param'], 'file_relative_path')
file_radc = get_config_item(config['file_param'], 'file_radcname')
file_ext = get_config_item(config['file_param'], 'file_ext')
sheet_name = get_config_item(config['file_param'], 'sheet_name')

########################## Main ##########################
# Define paths
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_file = os.path.join(path_incoming, file_relative_path, f"{file_radc}{file_ext}")

# Load data and upload to BigQuery
df = pd.read_excel(path_file, sheet_name=sheet_name)
pdbq.to_gbq(df, table_id, project_id=project_id)
print(f"Data from {sheet_name} in {path_file} uploaded to {table_id} in project {project_id}")
