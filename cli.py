import click
from openpyxl import Workbook, load_workbook
import os
import datetime


wb = load_workbook(filename = "expense_tracker.xlsx")
ws = wb.active

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



