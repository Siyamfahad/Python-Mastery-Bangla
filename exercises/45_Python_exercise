




#Build a number guessing game


import random

from sqlalchemy import false

print("welcome to number guessing game, pic a number between 1-10")

number = random.randint(1,10)
guess_limit = 0

run = True

while run:
    guess =int(input("enter the correct number : "))
    guess_limit +=1
    if guess_limit ==3:
        run = False
        print(f"you ran out of guess, the number was {number}")

    if guess > number:
        print("too high , try smaller")
    elif guess < number:
        print("too low, try higher")
    else:
        print(f"good job, the number was {number}, you took only {guess_limit} tries.")
        run = False

print("thanks for playing")
