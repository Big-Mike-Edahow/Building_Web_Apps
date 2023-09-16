# init_db.py

import sqlite3

connection = sqlite3.connect('./my_database.db')

with open('./schema.sql') as f:
    connection.executescript(f.read())

curs = connection.cursor()

# Insert rows of data into the backpacks table
curs.execute("INSERT INTO backpacks (make, model, price) VALUES ('Addidas', 'NYC Uptown', 17.99 );")

curs.execute("INSERT INTO backpacks (make, model, price) VALUES ('Nike', 'Arrow', 11.99);")

curs.execute("INSERT INTO backpacks (make, model, price) VALUES ('Nike', 'Sevilla', 13.99);")

curs.execute("INSERT INTO backpacks (make, model, price) VALUES ('Reebok', 'Streetsport', 11.99);")

connection.commit()
connection.close()

