import pandas as pd
#import warnings
import os 



#warnings.simplefilter(action='ignore', category=UserWarning)

input_filename = "input_lookml_meta.xlsx"
input_file_sheet = "input_lookml_meta"

output_filename = "output_auto_generated.txt"

data_incoming_foldername = 'data_incoming'
data_outgoing_foldername = 'data_outgoing'

path_script = os.path.realpath(__file__)
path_project = os.path.dirname(os.path.dirname(path_script))
path_incoming = os.path.join(path_project, data_incoming_foldername)
path_outgoing = os.path.join(path_project, data_outgoing_foldername)

input_file_path = os.path.join(path_incoming, input_filename)
output_file_path = os.path.join(path_outgoing, output_filename)


df = pd.read_excel(input_file_path, sheet_name=input_file_sheet)
#df['label'] = df['column_name'].str.title()

tab_len = 2
out_file_row_list =[]

### Default Dimensions ###
out_file_row_list.append((tab_len) * ' ' + '### Default Dimensions ### {')

for index, row in df.iterrows():
  out_file_row_list.append((tab_len ) * ' ' + 'dimension: {} '.format(row['column_name']) + '{')
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'type: {}'.format(row['looker_type']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'sql: ${{TABLE}}.{} ;;'.format(row['column_name']))

  out_file_row_list.append((tab_len ) * ' ' + '}')
  out_file_row_list.append('')
out_file_row_list.append((tab_len ) * ' ' + '### }')
out_file_row_list.append('')


    
out_txt_file = open(output_file_path, "w")
for row in out_file_row_list:
    print(row)
    out_txt_file.write("%s\n" % row)