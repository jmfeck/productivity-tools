' VBScript: excel_to_csv.vbs
Dim args, inputFile, outputFile, separator, decimal
Set args = WScript.Arguments

' Get input arguments
inputFile = args(0)
outputFile = args(1)

Dim excel
Set excel = CreateObject("Excel.Application")
excel.Visible = False
excel.DisplayAlerts = False

Dim workbook
Set workbook = excel.Workbooks.Open(inputFile)

' Save as CSV
Dim csvFormat
csvFormat = 6 ' FileFormat 6 is for CSV
workbook.SaveAs outputFile, csvFormat
workbook.Close False

excel.Quit
Set excel = Nothing
