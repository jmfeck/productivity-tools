# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: p.alor
"""

import os
import pandas as pd
from datetime import datetime

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.getcwd()
path_project = os.path.dirname(path_script)
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)


timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
inc_file_path = os.path.join(path_incoming, "gbu_sap_uploader.xlsx")
inc_sheet_name = 'gbu_arch_sap_uploader'

out_file_name_prefix = "gbu_sap_uploader_single_table"
out_file_name = f"{out_file_name_prefix}_{timestamp}.xlsx"
out_file_path = os.path.join(path_outgoing, out_file_name)

df = pd.read_excel(inc_file_path, sheet_name=inc_sheet_name)
df.to_excel(out_file_path, index=False)
