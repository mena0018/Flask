from flask import Flask

# Création de l’application :
app = Flask(__name__)


# Définition d’une fonction de "vue" accrochée
# au lien / (route)
@app.route("/")
def hello() -> str:
    return "Bonjour tout le monde ..!"


# Lancement de l’application
# On vérifie que l’application n’est pas lancée depuis un serveur Jupiter ou autre
if __name__ == "__main__":
    app.run()
