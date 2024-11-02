# BigQuery Excel Ingestion

This tool allows you to upload data from an Excel file to a Google BigQuery table. The configuration parameters are managed via a YAML file, making it easy to set up and customize.

## Features

- **Google BigQuery Integration**: Seamlessly uploads Excel data to a specified BigQuery table.
- **Configurable with YAML**: All parameters are set in a YAML configuration file for easy customization.
- **Automation Ready**: Ideal for automating data ingestion workflows.

## Requirements

- **Python 3.x**
- **Google Cloud SDK** with BigQuery permissions
- The following Python packages:
  - `pandas`
  - `pandas_gbq`
  - `PyYAML`
  - `gspread`

