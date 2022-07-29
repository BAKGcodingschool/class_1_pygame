#!/usr/bin/env python3
"""A simple guessing game.
"""
import random


MIN_NUM = 1
MAX_NUM = 100
NUM_GUESSES = 7


the_number = random.randint(MIN_NUM, MAX_NUM)

for attempt in range(NUM_GUESSES):
    print(f'Attempt #{attempt + 1} out of {NUM_GUESSES}:')
    the_guess = input(f'Guess a number between {MIN_NUM} and {MAX_NUM}: ')
    the_guess = int(the_guess)
    if the_guess > the_number:
        print('You are too high.')
    elif the_guess < the_number:
        print('You are too low.')
    else:
        print('You must be right!')
        break

print('Thank you for playing!')
