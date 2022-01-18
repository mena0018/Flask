# essais/test_movie.py
from movie import Movie

print("\nDurationToString")
print("----------------")

print(Movie.durationToString(512))
print(Movie.durationToString(4096))
print(Movie.durationToString(32768))

print("\nratingToStars")
print("--------------")
print(Movie.ratingToStars(0))
print(Movie.ratingToStars(2))
print(Movie.ratingToStars(4))
print(Movie.ratingToStars(8))
print(Movie.ratingToStars(100), "\n")

m1 = Movie('Les évadés', ["Drame"], 145, 9.5)
print(vars(m1))
print(dir(m1), "\n")

try:
    m2: Movie = Movie('Les évadés', ["Animation", "Action", "Aventure"],122, 5.5)
    print('Tout est OK.')
except:
    print('Les lignes précédentes n’auraient pas dû lancer d’exception !!')
try:
    m2 = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, -0.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!?")
try:
    m2 = Movie('Les évadés', ["Animation", "Action", "Aventure"], 122, 10.01)
    print('La ligne précédente aurait dû lancer une exception !!?')
except ValueError as e:
    print(f"L’exception \"{e}\" a bien été lancée.")
except:
    print("Ce n’est pas la bonne exception qui a été lancée !!? \n")

print("\nLe titre est    : ", m1.title)
print("La durée est de : ", m1.duration, "min")
print("La note est de  : ", m1.rating)
m1.rating = 9
print("La nouvelle note est de ", m1.rating)

m1: Movie = Movie('\n\nLes évadés', ["Drame"], 142, 9.3)
m2: Movie = Movie('\nLes indestructibles', ["Animation", "Action", "Aventure"], 115, 8.0)
print(m1)
print(m2)

print("\n\nTest de la méthode hasGenre : ")
print("-----------------------------")

print(m1.hasGenre("Drame"))
print(m1.hasGenre("Action"))
print(m2.hasGenre("Aventure"))
print(m2.hasGenre("Drame"))


