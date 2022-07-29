#!/usr/bin/env python3
"""A simple guessing game.
"""
the_number = 7
num_guesses = 5

for attempt in range(num_guesses):
    the_guess = input('Guess a number between 1 and 10: ')
    the_guess = int(the_guess)
    if the_guess > the_number:
        print('You are too high.')
    elif the_guess < the_number:
        print('You are too low.')
    else:
        print('That must be it!')

print('Thank you for playing!')
