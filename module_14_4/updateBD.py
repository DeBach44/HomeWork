import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price INTEGER NOT NULL
)
''')
connection.commit()
connection.close()

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

for i in range(1,5):
     cursor.execute("INSERT INTO Products(title, description, price)VALUES(?,?,?)",
                    (f'Продукт{i}', f'Описание{i}',  f'{i*500}'))

select_products = cursor.fetchall()
connection.commit()
connection.close()