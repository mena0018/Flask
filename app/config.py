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

    # Configuration d'un "pseudo" serveur mail
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['lebgdu_59200@hotmail.fr']

    # Configuration de la pagination
    POSTS_PAR_PAGE = 2
