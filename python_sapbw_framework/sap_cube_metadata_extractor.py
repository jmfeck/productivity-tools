# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 14:12:05 2024

@author: HH-FECK
"""

from pyrfc import Connection, ABAPApplicationError, ABAPRuntimeError
import pandas as pd

# Define the connection parameters for SAP using SNC and Logon Group
conn_params = {
    'mshost': 'PB1SAP.RCCAD.NET',        # SAP Message Server hostname
    'sysid': 'PB1',                      # System ID (e.g., "PB1")
    'client': '100',                     # Client number
    'group': 'PUBLIC',                   # Logon group (e.g., "PUBLIC")
    'snc_partnername': 'p:CN=HH-FECK@WORLD.MON',  # Your SNC name (for SSO authentication)
    'lang': 'EN',                        # Language (optional)
}


try:
    # Establish connection using SSO (SNC) and logon group
    conn = Connection(**conn_params)
    
    #cubes_result = conn.call('BAPI_MDPROVIDER_GET_CUBES')
    cube_name = 'Z6EASI/ZRI_CL_00_EAR_SAL_12'                 
        
    # Fetch variables
    variables_result = conn.call('BAPI_MDPROVIDER_GET_VARIABLES', CUBE_NAM=cube_name)
    variables_data = [
        {'Type': 'Variable', 'NAM': variable['VAR_NAM'], 'Description': variable['DSCRPTN']}
        for variable in variables_result['VARIABLES']
    ]

    # Fetch dimensions
    dimensions_result = conn.call('BAPI_MDPROVIDER_GET_DIMENSIONS', CUBE_NAM=cube_name)
    dimensions_data = [
        {'Type': 'Dimension', 'NAM': dimension['DIM_UNAM'], 'Description': dimension['DSCRPTN']}
        for dimension in dimensions_result['DIMENSIONS']
    ]

    # Fetch measures
    measures_result = conn.call('BAPI_MDPROVIDER_GET_MEASURES', CUBE_NAM=cube_name)
    measures_data = [
        {'Type': 'Measure', 'NAM': measure['MES_UNAM'], 'Description': measure['DSCRPTN']}
        for measure in measures_result['MEASURES']
    ]

    # Combine all data
    combined_data = variables_data + dimensions_data + measures_data

    # Create DataFrame
    df = pd.DataFrame(combined_data)

    # Define the file path for the Excel export
    export_path = 'sap_cube_structure.xlsx'

    # Export DataFrame to Excel
    df.to_excel(export_path, index=False)

    print(f"Data exported successfully to {export_path}")

except ABAPApplicationError as e:
    print(f"ABAP Application error occurred: {e}")
except ABAPRuntimeError as e:
    print(f"ABAP Runtime error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")