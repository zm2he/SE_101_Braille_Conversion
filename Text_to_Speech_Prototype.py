# Prototype program for testing espeak text to speech synthesizer
# importing espeak
from espeak import espeak
import os

#import subprocess if you want to use the last thing

# read input from user
teststring = raw_input()

# command for using espeak to synthesie teststring
os.system('espeak "{}"'.format(teststring))

    #           OR

#p = subprocess.Popen(['espeak', teststring])
