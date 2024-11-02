#!/bin/bash

# Run the Python script with the YAML configuration file and SQL query file as arguments
python scripts/bigquery_query_trigger.py config/sample_config.yaml queries/sample_query.sql

# Pause to keep the terminal open after execution
read -p "Press Enter to continue..."