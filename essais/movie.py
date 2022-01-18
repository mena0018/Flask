# Classe représentant un film.
class Movie:
    def __init__(self, _title: str, _genres: list, _duration: int, _rating: float = 0.0):
        self._title = _title
        self._genres = _genres
        self._duration = _duration
        self._rating = _rating

        if _rating < 0 or _rating > 10:
            raise ValueError("Valeur inférieur à 0 ou supérieur à 10")

    # Mise en place de la propriété “title” en lecture seule
    def _getTitle(self) -> str:
        return self._title

    @property
    def title(self) -> str:
        """
        Retourne le titre du film.
        Retour:
        Titre du film
        """
        return self._getTitle()

    # Mise en place de la propriété “duration” en lecture seule
    def _getDuration(self) -> int:
        return self._duration

    @property
    def duration(self) -> int:
        """
        Retourne la durée du film (exprimée en minutes).
        Retour:
        Durée du film
        """
        return self._getDuration()

    # Mise en place de la proprité “rating” en lecture et écriture
    def _getRating(self) -> float:
        return self._rating

    @property
    def rating(self) -> float:
        """
        Retourne la note donnée au film (comprise entre 0 et 10).
        Retour:
        Note du film
        """
        return self._getRating()

    @rating.setter
    def rating(self, r: float) -> None:
        """
        Modifie la note du film.
        La note doit être comprise entre 0 et 10
        Paramètre:
        r: nouvelle note du film (entre 0 et 10)
        """
        self._setRating(r)

    def _setRating(self, rating: float) -> None:
        """
        Modifie la note du film
        Paramètre:
        rating: nouvelle note du film
        Exception:
        ValueError: si la note n’est pas comprise entre 0 et 10
        """
        if rating < 0 or rating > 10:
            raise ValueError(f"Note {rating} inférieur à 0 ou supérieur à 10")
        else:
            self._rating = rating

    # Mise en place de la proprité “genres” en lecture seule
    def _getGenres(self) -> list:
        return self._genres

    @property
    def genres(self) -> list:
        """
        Retourne le genre d'un film.
        """
        return self._getGenres()

    def __repr__(self) -> str:
        minutes = self.durationToString(self.duration)
        genres = "/".join(self._genres)
        return f"{self.title} ({genres} - {minutes})\n {self.ratingToStars(int(self.rating))}"

    @staticmethod
    def durationToString(duration: int) -> str:
        return f"{duration // 60:02d}:{duration % 60:02d}"

    @staticmethod
    def ratingToStars(rating, max=10):
        noir = "\u2605"
        blanc = "\u2606"
        affichage = ''

        if rating >= 0 and rating <= max:
            for i in range(rating):
                affichage += noir
            for i in range(max - rating):
                affichage += blanc
        else:
            affichage = 'ERREUR : Choisissez un nombre compris entre 0 et 8'
        return affichage

    def hasGenre(self, text: str) -> bool:
        res = False
        for i in self._genres:
            if text == i:
                res = True
        return res
