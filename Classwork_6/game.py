import random
import os


def get_a_random_line(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, file_name)
    with open(file_path) as f:
        return random.choice([line for line in f.readlines()])

word = get_a_random_line('fruits.txt')
print(word)
# word = 'banana'

# print('Guess a number: ')
# print(' _ ' * len(word))