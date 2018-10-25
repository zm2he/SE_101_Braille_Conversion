from espeak import espeak
import os
#import subprocess if you want to use the last thing

teststring = raw_input()


os.system('espeak "{}"'.format(teststring))

    #           OR

#p = subprocess.Popen(['espeak', teststring])
