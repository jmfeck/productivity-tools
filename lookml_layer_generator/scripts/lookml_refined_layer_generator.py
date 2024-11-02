import pandas as pd
import warnings
import os

warnings.simplefilter(action='ignore', category=UserWarning)

input_filename = "input_lookml_meta.xlsx"
input_file_sheet = "input_lookml_meta"

output_filename = "output_refined_layer.txt"

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

df_dim = df[df['dim_or_measure'] == "dimension"]
df_dimgr = df[df['dim_or_measure'] == "dimension_group"]
df_mea = df[df['dim_or_measure'] == "measure"]

tab_len = 2
out_file_row_list =[]

### Default Dimensions ###
out_file_row_list.append((tab_len) * ' ' + '# -------------------------------')
out_file_row_list.append((tab_len) * ' ' + '# Default Dimensions')
out_file_row_list.append((tab_len) * ' ' + '# -------------------------------{')
for index, row in df_dim.iterrows():
  out_file_row_list.append((tab_len ) * ' ' + 'dimension: {} '.format(row['column_name']) + '{')
  #out_file_row_list.append((tab_len * 2 ) * ' ' + 'view_label: "{}"'.format(row['view_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'group_label: "{}"'.format(row['group_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'label: "{}"'.format(row['view_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'description: "{}"'.format(row['description'])) 
  out_file_row_list.append((tab_len ) * ' ' + '}')
  out_file_row_list.append('')
out_file_row_list.append((tab_len ) * ' ' + '### }')
out_file_row_list.append('')


### Default Measures ###
out_file_row_list.append((tab_len) * ' ' + '# -------------------------------')
out_file_row_list.append((tab_len) * ' ' + '# Default Measures')
out_file_row_list.append((tab_len) * ' ' + '# -------------------------------{')

for index, row in df_mea.iterrows():
  out_file_row_list.append((tab_len ) * ' ' + 'measure: {} '.format(row['column_name']) + '{')
  #out_file_row_list.append((tab_len * 2 ) * ' ' + 'view_label: "{}"'.format(row['view_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'group_label: "{}"'.format(row['group_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'label: "{}"'.format(row['view_label']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'description: "{}"'.format(row['description']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'type: {}'.format(row['type']))
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'sql: ${{{}}}'.format(row['column_name']) + " ;;")
  out_file_row_list.append((tab_len * 2 ) * ' ' + 'value_format_name: {}'.format(row['value_format_name']))
  out_file_row_list.append((tab_len ) * ' ' + '}')
  out_file_row_list.append('')
out_file_row_list.append((tab_len) * ' ' + '### }')
out_file_row_list.append('')

    
out_txt_file = open(output_file_path, "w")
for row in out_file_row_list:
    print(row)
    out_txt_file.write("%s\n" % row)