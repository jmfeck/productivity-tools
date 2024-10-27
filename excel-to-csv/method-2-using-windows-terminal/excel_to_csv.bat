::: Batch script: excel_to_csv.bat
@echo off

:: Enable delayed variable expansion
setlocal enabledelayedexpansion

:: Get the directory of the batch file
set "script_dir=%~dp0"

:: Define the folder containing Excel files relative to the script directory
set "input_folder=%script_dir%input"

:: Define the folder to store CSV output relative to the script directory
set "output_folder=%script_dir%output"

:: Create output folder if it doesn't exist
if not exist "%output_folder%" mkdir "%output_folder%"

:: Loop through all .xlsx files in the input folder
for %%f in (%input_folder%\*.xlsx) do (
    set "input_file=%%f"
    set "output_file=%output_folder%\%%~nf.csv"

    :: Print the input and output file paths for validation
    echo Input file: !input_file!
    echo Output file: !output_file!

    :: Run the VBScript to convert the file with the given separator and decimal symbol
    cscript //nologo excel_to_csv.vbs "!input_file!" "!output_file!"
    
    if !ERRORLEVEL! neq 0 (
        echo Conversion failed for !input_file!
    ) else (
        echo Conversion succeeded for !input_file!
    )
)

echo All files processed.
@pause
