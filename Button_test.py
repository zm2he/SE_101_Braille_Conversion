# GPIO imports
import RPi.GPIO as GPIO
import time

# Setup for GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # set pin numbering to BOARD, not BCM
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Setup for individual input pins
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# Array (simulating the braille array) for input from buttons to fill
test_array = [0, 0, 0, 0, 0, 0]

# Test function that reads (and debounces) input from a single button
def single_test():
    prev_input = GPIO.LOW
    input = GPIO.input(11)
    while prev_input ==GPIO.LOW and input != GPIO.HIGH:
        input = GPIO.input(11)
        if prev_input == GPIO.LOW and input == GPIO.HIGH:
            print("button pressed")
    prev_input = input
    time.sleep(0.05)
    print("Test Successful")

# Test function that reads input from a set of four buttons returns the value of the first button pressed
def reader():
    p_inpt = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW] # array for previous inputs
    inpt = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW] # array for current inputs
    press = 0 # flag to indicated whether button was pressed
    press_num = -1 # value of button pressed

    # get initial inputs
    for x in range(4):
        if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
            press = 1
            press_num = x

    # loop until there is an input
    while press == 0:
        # get inputs
        inpt[0] = GPIO.input(11)
        inpt[1] = GPIO.input(12)
        inpt[2] = GPIO.input(13)
        inpt[3] = GPIO.input(15)

        # see if anything is pressed
        for x in range(4):
            if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
                press = 1
                press_num = x

        # fill test array
        if press != 0:
            print(press_num)
            test_array[press_num] = 1

        # set previous inputs
        p_inpt[0] = inpt[0]
        p_inpt[1] = inpt[1]
        p_inpt[2] = inpt[2]
        p_inpt[3] = inpt[3]

        time.sleep(0.05) # time delay for debouncing

    return press_num

# function allowing continuous usage of reader function
def perp_reader():
    resultant = -1
    while resultant != 3:
        resultant = reader()
        test_array[resultant] = 1
        print(resultant)
    for x in test_array:
        print(x)

# test to be executed
perp_reader()
print("Okay, so let's get started")
for x in test_array:
    print(x)

"""
# Simple tests
# Simple input loop
while True: # Run forever
    if GPIO.input(11) == GPIO.HIGH:
        print("Button was pushed!")

# Input using callback method
def button1_callback(channel):
        print("Hooray Button 1");

def button2_callback(channel):
    print("Hooray Button 2");

GPIO.add_event_detect(11, GPIO.RISING, callback=button1_callback)
GPIO.add_event_detect(12, GPIO.RISING, callback=button2_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up

# Method for reading and debouncing 
prev_input = 0
while True:
    input = GPIO.input(11)
    if (not prev_input and input):
        print("button pressed")
    prev_input = input
    time.sleep(0.05)
# this is an endless for loop.
"""