import sqlite3 
con= sqlite3.connect("bank.db")
cur= con.cursor()
cur.execute("""CREATE TABLE if not exists Account(
    Name TEXT,
    Checkings REAL,
    Savings REAL,
    Pin REAL)""")
