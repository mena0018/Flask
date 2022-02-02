from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_moment import Moment

# Création de l’application
app = Flask(__name__)
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
# ainsi que celui des models
from app import routes, models

# Instanciation du module de gestion des dates
moment = Moment(app)

