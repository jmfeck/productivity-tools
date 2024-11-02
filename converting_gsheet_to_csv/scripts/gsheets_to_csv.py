# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 16:51:53 2022

@author: jfeck
"""

import os
import datetime
import gspread as gs
import pandas as pd
  
# ct stores current time
timestamp_str = datetime.datetime.now().strftime('%Y%m%d%H%M%S')

data_outgoing_foldername = 'data_outgoing'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_transformed = os.path.join(path_project, data_outgoing_foldername)

sheet_name_list = ['sample_gsheet_file'] #this is the tab name you want exported to a csv - remember, each tab will generate a different csv file
sheet_id = '1jqqWhkHNlF1SQOcG0unkRAbnJuCInCONy0Qz_pHLlSk' #this is the file id of the spreadsheet `workbook`

url = f'https://docs.google.com/spreadsheets/d/{sheet_id}'

gc = gs.service_account(filename='service_account_token.json')
sh = gc.open_by_url(url)

for sheet_name in sheet_name_list:
    filename = '_'.join([timestamp_str, sheet_name]) + '.csv'
    target_path = os.path.join(path_transformed, filename)
    ws = sh.worksheet(sheet_name)
    df = pd.DataFrame(ws.get_all_records())
    df.to_csv(target_path, index=False)


