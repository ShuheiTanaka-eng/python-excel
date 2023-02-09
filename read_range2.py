import openpyxl as excel

book = excel.load_workbook("cellname100.xlsx")
sheet = book.active

for row in sheet["C2":"F4"]:
    values = [cell.value for cell in row]
    print(values)

