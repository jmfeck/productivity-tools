import pandas as pd
import sys

def excel_to_csv(input_file, output_file, sep, decimal):
    try:
        # Read the Excel file
        df = pd.read_excel(input_file)
        # Save as CSV with specified separator and decimal
        df.to_csv(output_file, sep=sep, decimal=decimal, index=False)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python excel_to_csv.py <input_file.xlsx> <output_file.csv> <separator> <decimal>")
    else:
        excel_to_csv(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])