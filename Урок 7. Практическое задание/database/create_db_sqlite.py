import sqlite3

conn = sqlite3.connect('patterns.sqlite')   # связь с базой данных
cursor = conn.cursor()  # cursor - позволяет взаимодействовать с базой данных и добавлять записи
with open('create_db.sql', 'r') as f:
    text = f.read()
cursor.executescript(text)
cursor.close()
conn.close()
