from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index() -> str:
    user = {'username': 'Philippe'}
    # return render_template('index.html', title='Page principale', user=user)
    posts = [
        {
            'author': {'username': 'John'},
            'body': "Flask, c'est super !"
        },
        {
            'author': {'username': 'Suzan'},
            'body': "C'est encore mieux que Symfony ! Oups !"
        }
    ]
    return render_template('index.html', title='Accueil', user=user, posts=posts)


@app.route('/apropos')
def a_propos() -> str:
    return render_template('apropos.html', title="A Propos")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # Retourne false si le navigateur n'envoie pas de données mais renvoie les données
    # si l'utilisateur clique sur submit
    if form.validate_on_submit():
        flash(f"Enregistrement demandé pour l’utilisateur {form.username.data},"
              f" Se souvenir = {form.remember_me.data}")
        return redirect('/index')
    return render_template('login.html', title='Enregistrement', form=form)
