import sqlite3
con= sqlite3.connect('BondData.db')
# print("db is connected")
cur=con.cursor()
cur.execute("CREATE TABLE BOND(Bond_id INTEGER PRIMARY KEY AUTOINCREMENT,Bond_Number INTEGER,Bond_Prize INTEGER,Bond_Value INTEGER,Date)")
print("Creaated Table")