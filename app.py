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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles')
    articles = curse.fetchall()
    connect.close()
    return render_template('blog.html', articles = articles)

@app.route('/article/<int:article_id>')
def details(article_id):
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles WHERE id = ?', (article_id,))
    article = curse.fetchone()
    connect.close()
    return render_template('details.html', article=article)




@app.route('/profil/<string:auteur>')
def profil(auteur):
    connect = dbConnection()
    curse = connect.cursor()
    curse.execute('SELECT * FROM articles WHERE auteur = ?', (auteur,))
    aut = curse.fetchone()
    connect.close()
    return render_template('profil.html',aut = aut)

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
    return render_template('login.html')




if __name__ == '__main__':
    app.run(debug=True)