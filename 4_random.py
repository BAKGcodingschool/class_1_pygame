#!/usr/bin/env python3
"""A simple guessing game.
"""
import random


the_number = random.randint(1, 10)

num_guesses = 5

for attempt in range(num_guesses):
    print(f'Attempt #{attempt} out of {num_guesses}:')
    the_guess = input('Guess a number between 1 and 10: ')
    the_guess = int(the_guess)
    if the_guess > the_number:
        print('You are too high.')
    elif the_guess < the_number:
        print('You are too low.')
    else:
        print('You must be right!')
        break

print('Thank you for playing!')
