import click
from openpyxl import Workbook
import os
import datetime

wb = Workbook()
ws = wb.active
ws.title = "Expense Tracker"

# Row Titles
ws['A1'] = 'Variable Expenses'
ws['A2'] = 'Rent'
ws['A3'] = 'Gas'
ws['A4'] = 'Groceries'
ws['A5'] = 'Restaurants'
ws['A6'] = 'Student Loan'
ws['A6'] = 'Savings'
ws['A7'] = 'Recreation'

# Formatting
ws.column_dimensions['A'].width = 20
    
# Dates
ws['B2'] = datetime.datetime(2019, 1, 9).strftime("%m/%d/%y")

# Column Titles
ws['B1'] = 'Date'
ws['C1'] = 'Budgeted'
ws['D1'] = 'Spent'
ws['E1'] = 'Remaining'

for row in range(2, 8):
     for col in range(2, 5):
        _ = ws.cell(column=col, row=row, value="{0}".format("0"))


for row in range(2, 8):
     for col in range(5, 6):
        _ = ws.cell(column=col, row=row, value="{0}".format("=(C2:C7 - D2:D7)"))

# Budgeted amounts
ws['C2'] = 900
ws['C3'] = 200
ws['C4'] = 200

# Spent amounts

wb.save("expense_tracker.xlsx")

os.system("python3 spreadsheet.py")

        
@click.command()
@click.option('--category', prompt='Category', help='Category money was spent in.')
@click.option('--expense', prompt='You have spent', default=0.00, help='Amount spent.')
def spent(expense, category):
    """Simple program that tracks EXPENSES in various CATEGORIES."""
    click.echo('Spent ${:,.2f} on %s'.format(expense) % ( category))
    addSpent(category, expense)
    balance()
    

def addSpent(cat, amt):
    ws['D3'] = float(ws['D3'].value) + float(amt)
    wb.save("expense_tracker.xlsx")

def balance():
    totalAmt = float(ws['E3'].value)
    if totalAmt < 0:
        print("You are ${amt} over budget")
    elif totalAmt > 0:
        print("You have ${amt} remaining")
    else:
        print("You are at budget")

if __name__ == '__main__':
    spent()



