import click
import pandas as pd
from openpyxl import Workbook, load_workbook
import os
import datetime


wb = load_workbook(filename = "expense_tracker.xlsx")
ws = wb.active

os.system("python3 spreadsheet.py")
expenses = pd.read_excel("expense_tracker.xlsx")


        
@click.command()
@click.option('--category', prompt='Category', help='Category money was spent in.')
@click.option('--expense', prompt='You have spent', default=0.0, help='Amount spent.')

def categoryValid(expense, category):
    """Simple program that tracks EXPENSES in various CATEGORIES."""
    if category in expenses["Variable Expenses"].values:
        spent(expense, category)
    else:
        print("That is not a valid category")


def spent(expense, category):
        click.echo('Spent ${:,.2f} on %s'.format(expense) % ( category))
        addSpent(category, expense)
        balance(category)
    
def addSpent(cat, amt):
    if amt > 0:
        ws['D3'] = float(ws['D3'].value) + float(amt)
        wb.save("expense_tracker.xlsx")
    else: 
        print("Wait what the..!")

def balance(cat):
    chosenCategory = cat
    totalAmt = float(ws['C3'].value) - float(ws['D3'].value)
    if totalAmt < 0:
        print("You are $%.2f over budget for %s" % (totalAmt, chosenCategory))
    elif totalAmt > 0:
        print("You have $%.2f remaining for %s" % (totalAmt, chosenCategory))
    else:
        print("You are at budget for %s" % chosenCategory)

if __name__ == '__main__':
    categoryValid()



