movies = {'The Grinch': '11:00am',
          'Rudolph': '1:00pm',
          'Frosty the snow man': '3:15pm',
          'Christmas Vacation': '5:00pm',
          'Christmans with the Kranks':'7:20pm'}

print("We're showing the movies:")
for key in movies:
    print(key)

movie = input('What movie would you like the time for? ')

if movies.get(movie):
    print('\"', movie, '\" is playing at', movies[movie], sep='')
else:
    print('\"', movie, '\" is not on our list', sep='')