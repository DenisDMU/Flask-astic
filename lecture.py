import sqlite3

#Fonction en python pour pouvoir lire dans le terminal nos tables, mettre en commentaire la table que l'on ne veut pas voir
#sinon ça fait trop d'infos d'un coup je trouve et au moins, on sait si ce qu'on a fait est bien entré dans la DB

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


# cursor.execute("SELECT * FROM articles")
cursor.execute("SELECT * FROM contacts")
rows = cursor.fetchall()


for row in rows:
    print(row)


conn.close()

#python3 lecture.py pour voir qu'en effet, j'ai bien mes articles dedans mais aussi que ce que je rentre dans mon form contact y va :p