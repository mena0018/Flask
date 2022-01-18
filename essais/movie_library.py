from movie import Movie


# Classe représentant une collection de films
class MovieLibrary:
    # Constructeur de la classe MovieLibrary
    def __init__(self):
        self._movies = []

    # Reçoit en paramètre une instance de la classe Movie et ajoute ce film à la collection.
    def addMovie(self, film: Movie):
        self._movies.append(film)

    #  Retourne vrai si la collection contient un film ayant ce titre, faux sinon
    def containsMovieWithTitle(self, title: str) -> bool:
        res = False
        for i in self._movies:
            if title in i.title:
                res = True
        return res

