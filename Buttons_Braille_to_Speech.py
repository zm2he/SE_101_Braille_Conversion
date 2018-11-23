import RPi.GPIO as GPIO
import time

from espeak import espeak
import os

letter_codes = [[1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 1]]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

alphabet_size = 26

GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

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


# Function accepts a 6-element array representing a braille character and returns its corresponding character
# it does this by comparing the array with the given letter codes stored in an 2D array. The index of the corresponding
# code matches to the index of the character on a 1D array of letters; that string is returned
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
        #print(letter_codes[position][0], letter_codes[position][1], letter_codes[position][3], letter_codes[position][3], letter_codes[position][4], letter_codes[position][5])
    return letters[position]


# Function that allows use to input one braille character
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    max_points = 6
    input = button_reader()
    while max_points > 0 and input <6:
        if input < 6:
#            print(key_convert(keypad_input))
            letter_arr[input] = 1
            print(input)
            max_points -= 1
        if max_points > 0:
            input = button_reader()

    return [comparison(letter_arr),input]

# Function that allows user to imput word using input_letter
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
    while command < 8: # if 93is pressed after word entry, leave, else press a non -9 key
        i = input_word()
        sentence += i[0]
        print(i[0])
        command = i[1]
        sentence += " "
    print(sentence)
    return sentence

def text_to_speech ():
    teststring = input_sentence()
    os.system('espeak -ven+f3 -k5 -s 80 "{}"'.format(teststring))
text_to_speech()