import openpyxl as excel

book = excel.load_workbook("cellname100.xlsx")
sheet = book.active

it = sheet.iter_rows(
    min_row=2,max_row=4,min_col=3,max_col=6)

for row in it:
    values = [cell.value for cell in row]
    print(values)

    

