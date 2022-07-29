#!/usr/bin/env python3
"""A simple guessing game.
"""
import random


MIN_NUM = 1
MAX_NUM = 100
NUM_GUESSES = 7


def play_game():
    winner = False
    the_number = random.randint(MIN_NUM, MAX_NUM)

    print()
    for attempt in range(NUM_GUESSES):
        print(f'Attempt {attempt + 1} out of {NUM_GUESSES}')
        the_guess = None
        while not the_guess:
            the_guess = input(f'Guess a number between {MIN_NUM} and {MAX_NUM}: ')
            try:
                the_guess = int(the_guess)
            except ValueError:
                print('That is not a number! Try again.')
                the_guess = None

        if the_guess > the_number:
            print('You are too high.')
        elif the_guess < the_number:
            print('You are too low.')
        else:
            print('You are right!')
            winner = True
            break
    return winner


play_again = True
while play_again:
    winner = play_game()
    if not winner:
        print('Sorry, but you lost.')
    answer = input('Would you like to play again? (Y/n) ')
    if 'n' in answer.lower():
        play_again = False

print('Thank you for playing!')
