import sqlite3

db = sqlite3.connect('IntTransactionDB')
cursor = db.cursor()

def create_table( season ):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {season}( TransferDate TEXT, PlayerName TEXT, PrevTeam TEXT, CurrentTeam TEXT)')

def insert_data( season, date, name, prevt, currt):
    cursor.execute(f'INSERT INTO {season} VALUES( \'{date}\', \'{name}\', \'{prevt}\', \'{currt}\')')
    db.commit()

#create_table( 'Season20102011' )
#insert_data( 'Season20102011', '2019-01-01', 'Alex Caruso', 'Clippers', 'Lakers')

cursor.close()
db.close()