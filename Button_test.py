import RPi.GPIO as GPIO
import time

test_array = [0, 0, 0, 0, 0, 0]

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
"""
while True: # Run forever
    if GPIO.input(11) == GPIO.HIGH:
        print("Button was pushed!")
"""
"""
# using the callback method
def button1_callback(channel):
        print("Hooray Button 1");
        
def button2_callback(channel):
    print("Hooray Button 2");
    
GPIO.add_event_detect(11, GPIO.RISING, callback=button1_callback)
GPIO.add_event_detect(12, GPIO.RISING, callback=button2_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
"""


# returning input to our original functions
# use global variables that are altered?
# return function to output
# call an auxiliary function that 


"""
using the debounce method 
prev_input = 0
while True:
    input = GPIO.input(11)
    if (not prev_input and input):
        print("button pressed")
    prev_input = input
    time.sleep(0.05)
# this is an endless for loop.

"""
"""
prev_input = GPIO.LOW
input = GPIO.input(11)
while (prev_input ==GPIO.LOW and input != GPIO.HIGH):
    input = GPIO.input(11)
    if ((not prev_input) and input):
        print("button pressed")
    prev_input = input
    time.sleep(0.05)
print("Test Successful")

"""

def reader():
    p_inpt = [GPIO.LOW, GPIO.LOW, GPIO.LOW, GPIO.LOW]
    inpt = [GPIO.input(11), GPIO.input(12), GPIO.input(13), GPIO.input(15)]
    press = 0
    press_num = -1

    for x in range(4):
        if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
            press = 1
            press_num = x

    while press == 0:
        inpt = [GPIO.input(11), GPIO.input(12), GPIO.input(13), GPIO.input(15)]
        for x in range(4):
            if p_inpt[x] == GPIO.LOW and inpt[x] == GPIO.HIGH:
                press = 1
                press_num = x
        if press != 0:
            print(press_num+"button pressed")
        p_inpt = input
        time.sleep(0.05)

    return press_num

def perp_reader():
    resultant = -1;
    while resultant != 3:
        resultant = reader()
        print(resultant)