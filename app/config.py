# Classe de configuration
import os


# Dans le code ci-dessus, on recherche une variable d’environnement portant le nom SECRET_KEY qu’on
# affecte à l’attribut de classe SECRET_KEY. Si la variable d’environnement n’existe pas, c’est la chaîne de
# caractères 'un mot de passe à garder secret' qui sera utilisé.
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'un mot de passe à garder secret'
