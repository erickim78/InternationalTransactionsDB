import sqlite3

db = sqlite3.connect('IntTransactionDB')
cursor = db.cursor()

def create_table( season ):
    cursor.execute(f'CREATE TABLE IF NOT EXISTS {season}( TransferDate TEXT, PlayerName TEXT, PrevTeam TEXT, CurrentTeam TEXT)')

def insert_data( season, date, name, prevt, currt):
    cursor.execute(f'INSERT INTO {season} VALUES( {date}, {name}, {prevt}, {currt})')
    db.commit()




cursor.close()
db.close()