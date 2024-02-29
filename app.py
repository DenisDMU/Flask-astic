from flask import Flask, render_template, request, url_for,flash
import sqlite3



app = Flask(__name__)
app.secret_key = 'Donnez-moi-mon-formulaire' 

# La base de données
DATABASE = 'database.db'

#Pour se connecter à la DB
def dbConnection():
    connect = sqlite3.connect(DATABASE)
    connect.row_factory = sqlite3.Row
    return connect

#Route pour page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

#Route pour la page à propos
@app.route('/about')
def about():
    return render_template('about.html')

#Route pour le blog avec fonction (def en Python :p) pour fetch les infos stockés sur les articles dans la DB et pouvoir les display ensuite
@app.route('/blog')
def blog():
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles')
    articles = curse.fetchall()
    connect.close()
    return render_template('blog.html', articles = articles)

#Route pour la page détails de chaque article, avec ajout de l'id de l'article dans l'url et on fetchone pour un seul article
@app.route('/article/<int:article_id>')
def details(article_id):
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    article = curse.fetchone()
    connect.close()
    return render_template('details.html', article=article)



#Route pour le profil utilisateur, nom de l'auteur dans l'URL + fetchone pareil
@app.route('/profil/<string:auteur>')
def profil(auteur):
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles WHERE auteur = ?', (auteur,))
    aut = curse.fetchone()
    connect.close()
    return render_template('profil.html',aut = aut)

#Route de formulaire de contact avec ajax? pour stocker les infos récupérées en POST dans la DB dans la table contacts
@app.route('/contact', methods=['GET','POST'])
def contact():
    name = ""
    email = ""
    message = ""
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form ['email']
        message = request.form ['message']
        connect = sqlite3.connect('database.db')
        curse = connect.cursor()
        curse.execute("INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)", (name, email, message))
        connect.commit()
        flash(f"Votre demande de contact a été prise en compte.")
        connect.close()
    
    return render_template('contact.html')

# Faux compte pour le login (l'icone du bonhomme sur la navbar et pour faire un systeme de session)
@app.route('/login', methods= ['GET','POST'])
def login():
    #On peut ajouter en import en haut session, et ensuite je crois que c'est session. pour l'utiliser et définir son utilité
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)