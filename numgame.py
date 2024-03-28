#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num = random.randint(1, 100)
    rounds = 0
    guess = ""  # Initialize guess to None

    while rounds < 5 and guess != num:
        guess = input("Guess a number between 1 and 100\n>")
        
        if guess.isdigit():
            guess = int(guess)
        else:
            print("Please enter a valid number.")
            continue

        if guess > num:
            print("Too high!")
            rounds += 1  # Increment rounds
        elif guess < num:  # Use elif to handle this as a separate case
            print("Too low!")
            rounds += 1  # Increment rounds
        else:
            print("Correct!")
            break  # Exit the loop if the guess is correct

    if guess != num:
        print(f"Sorry, the number was {num}. Better luck next time!")

if __name__ == "__main__":
    main()
