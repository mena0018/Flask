# Classe de configuration
import os

basedir = os.path.abspath(os.path.dirname(__file__))


# Dans le code ci-dessus, on recherche une variable d’environnement portant le nom SECRET_KEY qu’on
# affecte à l’attribut de classe SECRET_KEY. Si la variable d’environnement n’existe pas, c’est la chaîne de
# caractères 'un mot de passe à garder secret' qui sera utilisé.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'un mot de passe à garder secret'

    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = \
        os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

