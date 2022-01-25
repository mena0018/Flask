from flask import Flask
from app.config import Config

# Création de l’application
app = Flask(__name__)

app.config.from_object(Config)

# On importe le fichier contenant la définition des fonctions de vue
from app import routes
