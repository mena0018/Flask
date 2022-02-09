from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

# Création de l’application
app = Flask(__name__)

# Chargement des variables de configuration depuis la classe Config
app.config.from_object(Config)

# Instanciation du module de gestion des connexions
login = LoginManager(app)
# Fonction de vue de redirection
login.login_view = 'login'
login.login_message = "Veuillez vous connecter"

# Démarrage du moteur de la base de données
db = SQLAlchemy(app)
# Démarrage de l'outil de migration associé à la base de données
migrate = Migrate(app, db)

# On importe le fichier contenant la définition des fonctions de vue
# de l’application et des erreurs ainsi que celui des models
from app import routes, models, erreurs

# Instanciation du module de gestion des dates
moment = Moment(app)

# Mise en place d'un gestionnaire de mails pour les messages d'erreur
if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Erreur dans MonApplication',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


# Ajout du gestionnaire de messages permettant de stocker
# les messages dans un ou plusieurs fichiers.
if not app.debug:
    # Création du répertoire pour les fichiers de log
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/mon_application.log', maxBytes=512000
                                       , backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s : %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Démarrage de MonApplication')
