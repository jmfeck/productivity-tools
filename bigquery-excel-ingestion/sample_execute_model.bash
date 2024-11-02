#!/bin/bash

# Run the Python script with the YAML configuration file as an argument
python scripts/ingest_excel_into_bigquery.py config/file_parameters.yaml

# Pause the terminal until the user presses Enter
read -p "Press Enter to continue..."