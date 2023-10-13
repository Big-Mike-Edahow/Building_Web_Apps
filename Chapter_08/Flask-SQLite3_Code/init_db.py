# init_db.py
# Initialize database and create table

import sqlite3

conn = sqlite3.connect('my_database.db')
curs = conn.cursor()

sql_query = '''
CREATE TABLE IF NOT EXISTS students (
    name STRING(20) NOT NULL,
    gender STRING(20),
    course STRING(20),
    mobile TEXT(10),
    username STRING(6) PRIMARY KEY NOT NULL,
    password TEXT(8) NOT NULL
);
'''

curs.execute(sql_query)

conn.commit()
conn.close()

