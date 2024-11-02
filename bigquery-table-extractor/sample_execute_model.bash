#!/bin/bash

# Run the Python script with the YAML configuration file as an argument
python scripts/bigquery_table_extractor.py config/sample_config.yaml

# Pause to keep the terminal open after execution
read -p "Press Enter to continue..."