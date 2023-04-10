from string import ascii_lowercase
import pandas as pd

n_letters = 5

def pretty_print(word):
    pretty_word = ''
    for char in word:
        pretty_word += ' {0}'.format(char)
    return pretty_word

def write_squares(filepath, list_of_words):
    with open(filepath, 'a+') as f:
        for word in list_of_words:
            f.write(pretty_print(word.upper()) + '\n')
        f.write('\n')

with open('words.txt', 'r') as f:
    all_words = [line.replace('\n', '').lower() for line in f.readlines()]

all_potential_words = [word for word in all_words if len(word) == n_letters and sum(
    [1 for char in word if char in ascii_lowercase]) == n_letters]
unique_potential_words = sorted(list(set(all_potential_words)))
valid_words = [
    word for word in unique_potential_words if word[::-1] in unique_potential_words]
palindromes = [word for word in valid_words if word[0]
               == word[-1] and word[1] == word[-2]]
words = [word for word in valid_words if word not in palindromes]

squares = []
for i, first_word in enumerate(words):
    possible_second_words = [word for word in words if word[0]
                             == first_word[1] and word[-1] == first_word[-2]]
    if len(possible_second_words) > 0:
        for j, second_word in enumerate(possible_second_words):
            possible_third_words = [
                word for word in palindromes if word[0] == first_word[2] and word[1] == second_word[2]]
            if len(possible_third_words) > 0:
                for k, third_word in enumerate(possible_third_words):
                    fourth_word = second_word[::-1]
                    fifth_word = first_word[::-1]
                    squares.append(
                        [first_word, second_word, third_word, fourth_word, fifth_word])
                    write_squares(
                        'sator_results.txt', [first_word, second_word, third_word, fourth_word, fifth_word])

print('Number of squares:', len(squares))
