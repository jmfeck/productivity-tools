# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: WCY8676
"""

import os
import logging
import win32com.client


data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'
log_foldername = 'logs'
log_filename = 'info.log'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)
path_log = os.path.join(path_project, log_foldername, log_filename)

logging.basicConfig(filename=path_log,level=logging.DEBUG)

''' 
# crawling through directory and subdirectories 
for root, directories, files in os.walk(path_incoming): 
    for filename in files: 
        # join the two strings in order to form the full filepath. 
        file_with_no_ext = filename.split('.')[0]
        inc_file_path = os.path.join(root, filename) 
        out_file_path =  os.path.join(path_outgoing, file_with_no_ext + '.xlsx') 
        file_params.append([inc_file_path, out_file_path, filename, file_with_no_ext]) 

for file_param in file_params:
    inc_file_path = file_param[0]
    out_file_path = file_param[1]
    filename = file_param[2]
    file_with_no_ext = file_param[3]
    
    logging.info(file_with_no_ext + ": starting")
    
    #reading excel
    logging.info(file_with_no_ext + ": importing data")
    dfstp0 = pd.read_csv(inc_file_path, dtype=str, sep=separator, decimal=dec, encoding=codec)

    #export to excel
    logging.info(file_with_no_ext + ": exporting to excel")
    dfstp0.to_excel(out_file_path, sheet_name=file_with_no_ext, index=False)
    logging.info(file_with_no_ext + ": finished")
'''

o = win32com.client.Dispatch("Excel.Application")
o.Visible = False

wb_filename = 'sample.xlsx'
inc_wb_path = os.path.join(path_incoming, wb_filename)

print(inc_wb_path)
wb = o.Workbooks.Open(inc_wb_path)
sheet_index_list = [0] #say you want to print these sheets

pdf_filename = 'sample.pdf'
out_pdf_path = os.path.join(path_outgoing, pdf_filename)

print_area = 'B2:I29'

for index in sheet_index_list:

    ws = wb.Worksheets[index]
    ws.PageSetup.Zoom = False
    ws.PageSetup.FitToPagesTall = 1
    ws.PageSetup.FitToPagesWide = 1
    ws.PageSetup.PrintArea = print_area
    #wb.WorkSheets(sheet_index_list).Select()
    wb.ActiveSheet.ExportAsFixedFormat(0, out_pdf_path)