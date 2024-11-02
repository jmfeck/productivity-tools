# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 15:38:26 2019

@author: WCY8676
"""

import zipfile
import os 

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)


# initializing empty file paths list 
file_paths = [] 
  
# crawling through directory and subdirectories 
for root, directories, files in os.walk(path_incoming): 
    for filename in files: 
        # join the two strings in order to form the full filepath. 
        file_with_no_ext = filename.split('.')[0]
        inc_file_path = os.path.join(root, filename) 
        out_file_path =  os.path.join(path_outgoing, file_with_no_ext + '.zip') 
        file_paths.append([inc_file_path, out_file_path, filename]) 
        
for file in file_paths:
    new_zip = zipfile.ZipFile(file[1], "w", zipfile.ZIP_DEFLATED)
    new_zip.write(file[0], file[2])
    new_zip.close()
    
