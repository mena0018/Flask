# essais/test_movie.py
from movie import durationToString, ratingToStars

print ("\nDurationToString")
print ("----------------")

print(durationToString(512))
print(durationToString(4096))
print(durationToString(32768))

print ("\nratingToStars")
print ("--------------")
print(ratingToStars(0))
print(ratingToStars(2))
print(ratingToStars(4))
print(ratingToStars(8))
print(ratingToStars(100))