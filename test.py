# Function accepts a keypad input and returns its corresponding spot on the 6-element array
def key_convert (num):
    key_position = [7, 8, 4, 5, 1, 2]
    i = 0
    while i <6 and key_position[i] != num:
        i += 1
    return i
"""
def print_braille(letter):
    for x in range(3):
        row = ""
        if letter[x*2] == 1:
            row += "*"
        else:
            row += "o"
        if letter[x*2 + 1] == 1:
            row += "*"
        else:
            row += "o"
        print(row)
"""
# Function accepts a 6-element array representing a braille character and returns its corresponding character
# it does this by comparing the array with the given letter codes stored in an 2D array. The index of the corresponding
# code matches to the index of the character on a 1D array of letters; that string is returned
def comparison (character):
    letter_codes = [[1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0],
                    [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0],
                    [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                    [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                    [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                    [1, 0, 0, 1, 1, 1]]
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
               "t", "u", "v", "w", "x", "y", "z"]
    i = 0
    found = 0
    position = 0 
    while i < 26 and found == 0:
        if letter_codes[i][0] == character[0] and letter_codes[i][1] == character[1] and letter_codes[i][2] == character[2] and letter_codes[i][3] == character[3] and letter_codes[i][4] == character[4] and letter_codes[i][5] == character[5]:
            position = i
            found = 1
        i = i + 1 #find a better sort/search function
    if found == 1:
        return letters[position]
    else:
        return " "

# Function that allows use to input one braille character
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    max_points = 6
    keypad_input = int(input())
    while max_points > 0 and keypad_input != 6:
        if keypad_input != 9 and keypad_input != 3 and keypad_input != 0:
            convert_spot = key_convert(keypad_input)
            print(convert_spot)
            letter_arr[convert_spot] = 1
            print(letter_arr[0], letter_arr[1], letter_arr[2], letter_arr[3], letter_arr[4], letter_arr[5])
            print(letter_arr[2])
            max_points = max_points - 1
        if max_points > 0:
            keypad_input = int(input())
    print(letter_arr[0], letter_arr[1], letter_arr[2], letter_arr[3],letter_arr[4],letter_arr[5])
    print(comparison(letter_arr))
    letter_arr = [0, 0, 0, 0, 0, 0]
    return comparison(letter_arr)

# Function that allows user to input a braille word
def input_word():
    word = ""
    command = 0
    while command != 9: # if 9 is pressed after letter entry, leave, else press a non -9 key
        letter = input_letter()
        word += letter
        print(letter)
        letter = 0
        print(word)
        command = int(input())
    return word

# Function that allows user to input a braille sentence
def input_sentence():
    sentence = ""
    command = 0
    while command != 3: # if 93is pressed after word entry, leave, else press a non -9 key
        word = input_word()
        sentence += word
        print(word)
        command = int(input())
        sentence += " "
    return sentence

print(input_letter())
#adsfdaf