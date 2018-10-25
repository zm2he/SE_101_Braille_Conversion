# Function accepts a keypad input and returns its corresponding spot on the 6-element array
def key_convert (num):
    key_position = [7,8,4,5,1,2]
    i = 0;
    while i <6 and key_position[i] != num:
        i+=1
    return i

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
    return letters[position]

# Function that allows use to input one braille character
def input_letter():
    letter_arr = [0, 0, 0, 0, 0, 0]
    max_points = 6
    keypad_input = int(input())
    while max_points > 0 and keypad_input != 6:
        if keypad_input != 9 and keypad_input != 3 and keypad_input != 0:
#            print(key_convert(keypad_input))
            letter_arr[key_convert(keypad_input)] = 1
            max_points -= 1
        if max_points > 0:
            keypad_input = int(input())
    return comparison(letter_arr)

#def input_word ()
#   word = ""
#   while :
#       word += input_letter()
#   return word

#print("Enter your name:")
#x = input();
#print("Hello" + x)
#print(input_letter())
