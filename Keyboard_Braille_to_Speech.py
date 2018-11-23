# espeak imports
from espeak import espeak
import os

# Global variables for storing alphabet, corresponding braille codes, and length of arrays
letter_codes = [[1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 1]]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

alphabet_size = 26

""" BRAILLE TO TEXT """
""" Braille is represented as [0, 1, 2, 3, 4, 5] which is 
[0 1
2 3
4 5]

or on the keypad
[7 8
4 5
1 2]
"""
""" Note that for input on the numeric keypad, "enter" must be pressed after every key is pressed. In order to end a 
letter, press 6. In order to end a word, press 9. In order to end a sentence, press 3."""

# Function which maps keys to spots on the braille array representation
def key_convert (num):
    key_position = [7, 8, 4, 5, 1, 2]
    place = -1
    if num == 7:
        place = 0
    elif num == 8:
        place = 1
    elif num == 4:
        place = 2
    elif num == 5:
        place = 3
    elif num == 1:
        place = 4
    elif num == 2:
        place = 5
    else:
        place = -1
    return place

# Function accepts a braille character array and returns its matching alphabetic character
# returns a zero-length string if a matching letter is not found
def comparison (character):
    i = 0
    found = 0
    position = 0
    while i < alphabet_size and found == 0:
        j = 0
        similarity = 1
        while j < 6:
            if letter_codes[i][j] != character[j]:
                similarity = 0
                break
            j += 1
        if similarity == 1:
            position = i
            found = 1
            break
        i += 1

    if similarity == 0:
        return ""
    else:
        return letters[position]


# Function that allows use to input one braille character using the keypad
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    keypad_input = int(input())
    while keypad_input != 6 and keypad_input != 9 and keypad_input !=3: # press 6 to exit letter
        if keypad_input != 9 and keypad_input != 3 and keypad_input != 0:
            conversion = key_convert(keypad_input)
            if conversion >= 0:
                letter_arr[key_convert(keypad_input)] = 1
            keypad_input = int(input())

    return [comparison(letter_arr),keypad_input]

# Function that allows user to input word using input_letter()
def input_word():
    word = ""
    command = 0
    while (command != 9 and command != 3): # press 9 to exit word
        i = input_letter()
        word += i[0]
        command = i[1]
    return [word, command]

# Function that allows user to input sentence using input_word()
def input_sentence():
    sentence = ""
    command = 0
    while command != 3: # if press 3 to exit sentence
        i = input_word()
        sentence += i[0]
        print(i[0])
        command = i[1]
        sentence += " "
    return sentence

#       Text to Speech
def text_to_speech ():
    teststring = input_sentence()
    os.system('espeak -ven+f3 -k5 -s 80 "{}"'.format(teststring))
text_to_speech()