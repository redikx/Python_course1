import random

highest=10
winningNumber = random.randint(1,highest)

guess=11
while guess != 0:
    guess=int(input("Enter your guess "))
    if guess > winningNumber:
        print("Too high, try lower")
    if guess < winningNumber and guess != 0:
        print("Too low, try higher")
    if guess == winningNumber:
        print("You won, correct was : {0}".format(guess))
        break

