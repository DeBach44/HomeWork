import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL 
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     balance = 1000
#     cursor.execute("INSERT INTO Users(username, email, age, balance)VALUES(?,?,?,?)",
#                    (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', f'{balance}'))
#
# for i in range(1,11,2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', ('500',i))
#
#
# for i in range(1,11,3):
#     cursor.execute('DELETE FROM Users WHERE id = ?',(i,))

# cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
# select_users = cursor.fetchall()
# for user in select_users:
#     print(f"Name: {user[0]}, email: {user[1]}, Age: {user[2]}, Balance: {user[3]}")

# cursor.execute('DELETE FROM Users WHERE id = 6') #Удаление

cursor.execute('SELECT COUNT(*) FROM Users') #Запрос количества записей
total_users = cursor.fetchone()[0]

cursor.execute('SELECT SUM(balance) FROM Users') #Сумма балансов
all_balances = cursor.fetchone()[0]

print(all_balances / total_users)

connection.commit()
connection.close()
