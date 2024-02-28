import sqlite3

conn = sqlite3.connect('databasefile.db')
cr = conn.cursor()

cr.execute("""
            CREATE TABLE IF NOT EXISTS Movies (
           id INTEGER PRIMARY KEY,
           title TEXT,
           director TEXT,
           year INTEGER,
           genre TEXT)            
            """)
# table should be created with those attribute/column names