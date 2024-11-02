# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import yaml
import sys
import pandas as pd
import pandas_gbq as pdbq
import os
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

###############################################################################################################
# Config file reader
###############################################################################################################
def load_config(file_path):
    """Load configuration from a YAML file."""
    with open(file_path, 'r') as file:
        config = yaml.safe_load(file)
    logging.info(f"Configuration loaded from {file_path}")
    return config

conn_config_file_path = sys.argv[1]
config = load_config(conn_config_file_path)

###############################################################################################################
# Functions
###############################################################################################################
def get_config_item(config_section, var):
    """Retrieve a configuration item and ensure it's not empty."""
    try:
        val = config_section[var]
        if not val:
            raise ValueError(f"{var} cannot be an empty string")
        logging.info(f"{var}: {val}")
        return val
    except KeyError as e:
        logging.error(f"Missing configuration for {var}")
        sys.exit(1)

###############################################################################################################
# Get config values
###############################################################################################################
project_id = get_config_item(config['bq_param'], 'project_id')
dataset = get_config_item(config['bq_param'], 'dataset')
tablename = get_config_item(config['bq_param'], 'tablename')
table_id = f"{project_id}.{dataset}.{tablename}"

data_outgoing_foldername = get_config_item(config['project_param'], 'data_outgoing_foldername')
file_relative_path = get_config_item(config['file_param'], 'file_relative_path')
file_radc = get_config_item(config['file_param'], 'file_radcname')
file_ext = get_config_item(config['file_param'], 'file_ext')
file_sheetname = get_config_item(config['file_param'], 'sheet_name')

###############################################################################################################
# Path Handling
###############################################################################################################
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_outgoing = os.path.join(path_project, data_outgoing_foldername, file_relative_path)
os.makedirs(path_outgoing, exist_ok=True)
path_file = os.path.join(path_outgoing, f"{file_radc}{file_ext}")

###############################################################################################################
# Main Process
###############################################################################################################
logging.info("Reading table from BigQuery")
sql = f"SELECT * FROM {table_id}"
df = pdbq.read_gbq(sql, project_id=project_id)

logging.info("Exporting table")
exporters = {
    ".parquet": lambda df, path: df.to_parquet(path, index=False),
    ".csv": lambda df, path: df.to_csv(path, index=False),
    ".xlsx": lambda df, path: df.to_excel(path, sheet_name=file_sheetname, index=False)
}

try:
    exporters[file_ext](df, path_file)
    logging.info(f"Table exported successfully to {path_file}")
except KeyError:
    logging.error(f"Unsupported file extension: {file_ext}")
