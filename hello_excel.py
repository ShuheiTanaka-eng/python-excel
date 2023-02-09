import openpyxl as excel

book = excel.Workbook()

sheet = book.active

sheet["A1"] = "こんにちは、Excel"
sheet["A2"] = "やっほう"
sheet["A3"] = "ありがとう"
sheet["A4"] = "美味しい"
sheet["A5"] = "楽しい"

book.save("hello.xlsx")
