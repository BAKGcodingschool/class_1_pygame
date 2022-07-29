#!/usr/bin/env python3
"""A simple guessing game.
"""
the_number = 7

print('Guess a number between 1 and 10:')
the_guess = input()

the_guess = int(the_guess)
if the_guess == the_number:
    print('You were right!')
elif the_guess > the_number:
    print('You were too high.')
elif the_guess < the_number:
    print('You were too low.')

print('Thank you for playing!')
