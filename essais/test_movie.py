# essais/test_movie.py
from movie import durationToString, ratingToStars
from movie import Movie

print("\nDurationToString")
print("----------------")

print(durationToString(512))
print(durationToString(4096))
print(durationToString(32768))

print("\nratingToStars")
print("--------------")
print(ratingToStars(0))
print(ratingToStars(2))
print(ratingToStars(4))
print(ratingToStars(8))
print(ratingToStars(100), "\n")

# ...
m1 = Movie('Les évadés')
print(vars(m1))
print(dir(m1), "\n")
