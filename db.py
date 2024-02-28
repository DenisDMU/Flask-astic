import sqlite3

#Pour se connecter à la DB
connection = sqlite3.connect('database.db')
co = connection.cursor()
co.execute('DROP TABLE IF EXISTS articles')
co.execute('DROP TABLE IF EXISTS contacts')

#Création des tables, articles et celle du formulaire
co.execute('''CREATE TABLE articles
           (id INTEGER PRIMARY KEY AUTOINCREMENT,
           titre TEXT,
           extrait TEXT,
           contenu TEXT,
           image_article TEXT,
           profil_pic TEXT,
           auteur TEXT)''')

co.execute('''CREATE TABLE contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            message TEXT)''')

connection.commit()
connection.close()