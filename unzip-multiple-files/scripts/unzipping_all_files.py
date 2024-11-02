# -*- coding: utf-8 -*-

# ==============================================================================
#   Author: João Manoel Feck
#   Email: joaomfeck@gmail.com
#   GitHub: https://github.com/jmfeck
# ==============================================================================

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
        file_paths.append([inc_file_path, filename]) 
        
for file in file_paths:
    new_unzip = zipfile.ZipFile(file[0], "r")
    new_unzip.extractall(path_outgoing)
    new_unzip.close()
    
