import re

from typing import Tuple

def char_position(letter:str):
    letter_index = (ord(letter.lower()) - 97) + 1
    if letter.isupper():
        letter_index += 26
    return letter_index

def split_word_to_two_equal_length_words(word: str) -> Tuple[str, str]:
    characters_count = len(word)
    middle_index = int(characters_count/2) 
    return word[0:middle_index], word[middle_index:characters_count]

def find_matching_letter(left_word:str, right_word:str) -> str:
    for w in left_word:
        if w not in right_word:
            continue

        return w

def main():
    # f = open("input_demo.txt", "r")
    f = open("input.txt", "r")
    words = re.split('\n', f.read())

    sum = 0
    for word in words:
        left, right = split_word_to_two_equal_length_words(word)
        matching_letter = find_matching_letter(left, right)
        sum += char_position(matching_letter)

    print(sum)

if __name__ == "__main__":
    main()

