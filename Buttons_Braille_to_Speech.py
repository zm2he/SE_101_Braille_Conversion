# GPIO imports
import RPi.GPIO as GPIO
import time

# espeak imports
from espeak import espeak
import os

# GPIO setup
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Global variables to store the alphabet, corresponding braille codes, and size
letter_codes = [[1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 1]]

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

alphabet_size = 26

""" BUTTON INPUT READING """

# Button reading function
def button_reader():
    p_inpt = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
    inpt = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
    press = 0
    press_num = -1

    for x in range(4):
        if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
            press = 1
            press_num = x

    while press == 0:
        inpt[0] = GPIO.input(11)
        inpt[1] = GPIO.input(12)
        inpt[2] = GPIO.input(13)
        inpt[3] = GPIO.input(15)
        for x in range(4):
            if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
                press = 1
                press_num = x

        if press != 0:
            print(press_num)
        p_inpt[0] = inpt[0]
        p_inpt[1] = inpt[1]
        p_inpt[2] = inpt[2]
        p_inpt[3] = inpt[3]
        time.sleep(0.05)

    return press_num

""" BRAILLE TO TEXT CONVERSION"""

# Function accepts a braille character array and returns its matching alphabetic character
# returns a zero length string if matching letter is not found
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

    if found == 0:
        return ""
    else:
        return letters[position]


# Function that allows use to input one braille character
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    input = button_reader()
    while input <6:
        if input < 6:
            letter_arr[input] = 1
#            print(input)
            input = button_reader()
    return [comparison(letter_arr),input]

# Function that allows user to input word using input_letter
def input_word():
    word = ""
    command = 0
    while command < 7:
        i = input_letter()
        word += i[0]
        command = i[1]
    print(word)
    return [word, command]

# Function that allows user to input sentence using input_letter
def input_sentence():
    sentence = ""
    command = 0
    while command < 8:
        i = input_word()
        sentence += i[0]
        print(i[0])
        command = i[1]
        if command == 8:
            sentence += " "
    print(sentence)
    return sentence

""" TEXT TO SPEECH CONVERSION """
def text_to_speech ():
    teststring = input_sentence()
    os.system('espeak -ven+f3 -k5 -s 80 "{}"'.format(teststring))


""" EXECUTING FINAL PROGRAM """
text_to_speech()