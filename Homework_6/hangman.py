import os
import random


def get_a_random_line(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path) as f:
        return random.choice([line for line in f.readlines()]).rstrip()


def start():
    word = get_a_random_line('fruits.txt')
    
    word = word.upper()
    letters = set(word)
    guessed = set()
    mistake = 0

    while mistake < 5:
        if guessed.issuperset(letters):
            for letter in word:
                print(f' {letter} ', end='')

            print()
            print('You won the game.')
            break

        print(f'Guess the word. {5 - mistake} mistakes left.')

        for letter in word:
            if letter in guessed:
                print(f' {letter} ', end='')
            else:
                print(' _ ', end='')

        print()
        guess = input('Guess a letter: ').upper()
        guessed.add(guess)

        if guess not in letters:
            mistake += 1


start()
