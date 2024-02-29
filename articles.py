#Vu qu'il n'y a pas de demande de forms ou autres methodes d'injection des articles, je vais le faire ici en INSERT SQL

import sqlite3

connect = sqlite3.connect('database.db')
cursor = connect.cursor()

#Création d'auteur, chacun ont 2 articles donc j'ai décidé de les placer dans une constante
same_auteur = 'MintAddict'
same_auteur2 = 'CoffeCacaoAndAll'

#Création de faux articles a rentrer dans la DB
articles = [
    ('La menthe','Decouvrez son histoire',
     'Depuis des années, la menthe est au coeur de nos vies. Son gout frais, mais aussi sa douceur ne font qu\'un pour nous émerveiller.',
     'static/blog/imgart1.jpg','static/blog/pp1.png',same_auteur
     ),
    ('La Fraise','Rouge comme une fraise',
     'Ramène ta fraise ! Ici, on adore la fraise. On peut en faire des tartes, de la confiture, mais aussi et surtout des bons milkshake bien frais. C\'est tout ce qu\'on adore ici',
     'static/blog/imgart2.jpg','static/blog/pp1.png',same_auteur),
    ('Le café','L\'or noir',
     'Que dire de plus. Le café, l\'or noir, le plus beau. Cette essence vitale chaque maintenant qui fait que nous sommes si heureux et réveillés. Sans lui, nos journées serait bien longues. Partagez avec moi l\'amour du café',
     'static/blog/imgart3.jpg','static/blog/pp2.jpeg',same_auteur2),
    ('Le chocolat','Cacao et guimauves',
     'Chaud cacao, chaud chaud chocolat. Et oui, la douceur de l\'enfance, celui qui nous a bercé. Le bon chocolat chaud, celui qui vous a accompagné pendant les différents goûters de votre jeunesse. Petit point en plus s\'il s\'agissait du chocolat chaud Mercier !',
     'static/blog/imgart4.jpg','static/blog/pp2.jpeg',same_auteur2)
]

#Je boucle sur mes articles pour les rentrer un par un dans la DB avec les infos dans les bonnes colonnes
for article in articles:
    cursor.execute('''INSERT INTO articles (titre,extrait,contenu,image_article,profil_pic,auteur) VALUES(?,?,?,?,?,?)''',article)
   
#Je commit ma requête et ensuite cloture la connexion à la DB 
connect.commit()
connect.close()