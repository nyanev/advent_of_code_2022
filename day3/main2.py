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

def find_matching_letter(first:str, second:str, third: str) -> str:
    for w in first:
        if w  in second and w  in third:
            return w

def main():
    # f = open("input_demo.txt", "r")
    f = open("input.txt", "r")
    words = re.split('\n', f.read())

    sum = 0
    for i, word in enumerate(words):
        if i % 3 != 0:
            continue
        first = word
        second = words[i+1:i+2][0]
        third = words[i+2:i+3][0]

        matching_letter = find_matching_letter(first, second, third)
        sum += char_position(matching_letter)

    print(sum)

if __name__ == "__main__":
    main()

