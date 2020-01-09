import click


        
@click.command()
@click.option('--category', prompt='In category of', help='Category money was spent in.')
@click.option('--expense', prompt='You have spent', default=0.00, help='Amount spent.')
def spent(expense, category):
    """Simple program that tracks EXPENSES in CATEGORIES."""
    click.echo('Spent ${:,.2f} on %s'.format(expense) % ( category))

if __name__ == '__main__':
    spent()

