# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

import os
import datetime
import gspread as gs
import pandas as pd
import yaml

# Load configuration from YAML
config_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'config', 'config.yaml')
with open(config_path, 'r') as config_file:
    config = yaml.safe_load(config_file)

# Extract parameters from config
data_outgoing_foldername = config['project_param']['data_outgoing_foldername']
sheet_name_list = config['gsheet_param']['sheet_name_list']
sheet_id = config['gsheet_param']['sheet_id']
service_account_file = config['gsheet_param']['service_account_file']

# Generate timestamp
timestamp_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

# Define paths
path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_transformed = os.path.join(path_project, data_outgoing_foldername)
os.makedirs(path_transformed, exist_ok=True)

# URL for Google Sheet
url = f'https://docs.google.com/spreadsheets/d/{sheet_id}'

# Google Sheets API client setup
gc = gs.service_account(filename=service_account_file)
sh = gc.open_by_url(url)

# Export each sheet to CSV
for sheet_name in sheet_name_list:
    filename = f"{timestamp_str}_{sheet_name}.csv"
    target_path = os.path.join(path_transformed, filename)
    ws = sh.worksheet(sheet_name)
    df = pd.DataFrame(ws.get_all_records())
    df.to_csv(target_path, index=False)
    print(f"Exported {sheet_name} to {target_path}")
