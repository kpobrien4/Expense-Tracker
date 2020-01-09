from openpyxl import Workbook
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
ws.title = "Expense Tracker"
ws['A1'] = 'Rent'

for x in range(1,101):
       for y in range(1,101):
           ws.cell(row=x, column=y)

ws['B1'] = 27
ws['C1'] = 14


ws['D1'] = "=SUM(B1, C1)"

wb.save("expense_tracker.xlsx")
