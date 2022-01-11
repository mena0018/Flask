# Convertit une durée exprimée en minutes en une chaîne de caractères * ayant la
# forme HH:MM
# Si nécessaire, le nombre d'heures peut comporter plus de 2 chiffres.
# param $minutes durée en minutes
# return résultat

def durationToString(minutes: int) -> str :
    heure = ((minutes / 60) - (minutes % 60) / 60)
    minutes = minutes % 60
    print(int(heure), ":", minutes)


