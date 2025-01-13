#Ava Mendoza
#Number Guesser
import random

def guess_the_number(random):
    print("Welcome to the Number Guesser")
    ans = input("Guess the number between 1 and 10, you have 3 guesses")

    if str(ans) == str(random):
        print("Congratulations! You guessed the number.")
    if str(ans) < str(random):
        print("Your guess is too low, try again")
    if str(ans) > str(random):
        print("Your guess is too high, try again")
    ans = input("Guess the number between 1 and 10, you have 2 guesses left")
    if str(ans) == str(random):
        print("Congratulations! You guessed the number.")
    if str(ans) < str(random):
        print("Your guess is too low, try again")
    if str(ans) > str(random):
        print("Your guess is too high, try again")
    ans = input("Guess the number between 1 and 10, This is your last guess")
    if str(ans) == str(random):
        print("Congratulations! You guessed the number.")
        quit()
    else:
        print("Sorry, that is not the correct answer. The number was"+" "+ str(random)+".")
    print("Thanks for playing!")

guess_the_number(random.randint(1,10))

