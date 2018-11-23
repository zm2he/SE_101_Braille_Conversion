letter_codes = [[1, 0, 0, 0, 0, 0], [1, 0, 1, 0, 0, 0], [1, 1, 0, 0, 0, 0], [1, 1, 0, 1, 0, 0], [1, 0, 0, 1, 0, 0],
                [1, 1, 1, 0, 0, 0], [1, 1, 1, 1, 0, 0], [1, 0, 1, 1, 0, 0], [0, 1, 1, 0, 0, 0], [0, 1, 1, 1, 0, 0],
                [1, 0, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0], [1, 0, 0, 1, 1, 0],
                [1, 1, 1, 0, 1, 0], [1, 1, 1, 1, 1, 0], [1, 0, 1, 1, 1, 0], [0, 1, 1, 0, 1, 0], [0, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 0, 0, 1, 1], [1, 1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1, 1]]
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
           "t", "u", "v", "w", "x", "y", "z"]

# Function accepts a keypad input and returns its corresponding spot on the 6-element array
def key_convert (num):
    key_position = [7,8,4,5,1,2]
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

    #i = 0
    #while i <6 and key_position[i] != num:
        #i+=1
    #return i

# Function accepts a 6-element array representing a braille character and returns its corresponding character
# it does this by comparing the array with the given letter codes stored in an 2D array. The index of the corresponding
# code matches to the index of the character on a 1D array of letters; that string is returned
def comparison (character):
    i = 0
    found = 0
    position = 0
    while i < 26 and found == 0:
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
    if (found == 0):
        return ""
    else:
        return letters[position]

def reverse_compare(character):
    i = 0
    found = 0
    position = 0
    while i < 26 and found == 0:
        if character == letters[i]:
            position = i
            found = 1
            break
        i += 1
        #print(letter_codes[position][0], letter_codes[position][1], letter_codes[position][3], letter_codes[position][3], letter_codes[position][4], letter_codes[position][5])
    return letter_codes[position]

# Function that allows use to input one braille character
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    max_points = 6
    keypad_input = int(input())
    while max_points > 0 and keypad_input != 6 and keypad_input != 9 and keypad_input !=3:
        if keypad_input != 9 and keypad_input != 3 and keypad_input != 0:
#            print(key_convert(keypad_input))
            letter_arr[key_convert(keypad_input)] = 1
            print(key_convert(keypad_input))
            max_points -= 1
        if max_points > 0:
            keypad_input = int(input())

    return [comparison(letter_arr),keypad_input]

def input_word():
    word = ""
    command = 0
    while (command != 9 and command != 3):
        i = input_letter()
        word += i[0]
        command = i[1]
    return [word, command]

def input_sentence():
    sentence = ""
    command = 0
    while command != 3: # if 93is pressed after word entry, leave, else press a non -9 key
        i = input_word()
        sentence += i[0]
        print(i[0])
        command = i[1]
        sentence += " "
    return sentence

def plus_one(num):
    asef = num + 1;
    return asef;

def twoplus():
    print(plus_one(int(input())))
    print(plus_one(int(input())))

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

#def input_word ()
#   word = ""
#   while :
#       word += input_letter()
#   return word

#print("Enter your name:")
#x = input();
#print("Hello" + x)
print(print_braille(reverse_compare("b")))
