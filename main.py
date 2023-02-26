from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy'or 'difficult': ").lower()

if difficulty == 'easy':
    attempts = 10
elif difficulty == 'difficult':
    attempts = 5

number = random.randint(1, 100)
print(number)


def guessingGame():
    numero = attempts
    while numero > 0:
        print(f"You have {numero} remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess != number:
            if guess > number:
                print("Too high")
            else:
                print("Too low")
            print("Guess again!")
        else:
            print("You won!")
            break
        numero = numero - 1
        
guessingGame()