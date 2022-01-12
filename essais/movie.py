# Convertit une durée exprimée en minutes en une chaîne de caractères * ayant la
# forme HH:MM
# Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
# param $minutes durée en minutes
# return résultat

def durationToString(minutes: int) -> str:
    heure = minutes // 60
    minutes = minutes % 60

    if heure < 10:
        heure = '0' + str(heure)

    if minutes < 10:
        minutes = '0' + str(minutes)

    return str(heure) + ":" + str(minutes)


# Convertit une note entière comprise entre 0 et $max en une chaîne de caractères
# composée d'étoiles.
# param $rating note comprise entre 0 et $max
# param $max valeur maximale de la note
# return chaîne de caractères composée d'étoiles

def ratingToStars(rating, max=8):
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


# Classe représentant un film.
class Movie:
    def __init__(self, _title: str, _duration: int, _rating: float = 0.0):
        self._title = _title
        self._duration = _duration
        self._rating = _rating

        if _rating < 0 or _rating > 10:
            raise ValueError("Valeur inférieur à 0 ou supérieur à 10")

    def getTitle(self) -> str:
        return self._title

    def getDuration(self) -> int:
        return self._duration

    def getRating(self) -> float:
        return self._rating

    def setRating(self, newRating):
        if newRating < 0 or newRating > 10:
            raise ValueError("Valeur inférieur à 0 ou supérieur à 10")
        else:
            self._rating = newRating

