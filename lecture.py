import sqlite3


conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# cursor.execute("SELECT * FROM articles")
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()

#python3 lecture.py pour voir qu'en effet, j'ai bien mes articles dedans mais aussi que ce que je rentre dans mon form contact y va :p