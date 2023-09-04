import random as rd

roll = rd.randint(1, 6)

guess = int(input("Guess the roll: "))

if guess == roll:
    print("Correc! the roll was " + str(roll))
else:
    print("Incorrect! the roll was " + str(roll))