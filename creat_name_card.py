import xlrd
from docxtpl import DocxTemplate

excel = xlrd.open_workbook("name.xls")
sheet = excel.sheets()[0]
doc = DocxTemplate("template.docx")

for i in range(sheet.nrows):
    name = sheet.cell_value(i, 1)
    work = sheet.cell_value(i, 2)
    doc.render({"name": name, "work":work})
    doc.save(f'{name}.docx')