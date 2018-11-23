# Brailliant

Real-time Braille to Speech Converter - To allow blind and deaf people to live a more accesible life!

### Prerequisites

* Raspberry Pi booted on Raspbian OS
* Espeak
* Alsa
* An IDE for Python 2


### Installation


Getting Alsa ready
```
sudo apt-get install alsa-utils
sudo amixer cset numid=0
sudo amixer cset numid=1
```
Getting Espeak
```
sudo apt-get install espeak
```

## Running the tests
Our system currently accepts inputs by push buttons and numerical keypad inputs.

# Keypad Input
We have mapped the braille array to the numerical keypad in the following manner:
```
7 8
4 5
1 2
```

Each key corresponds to an entry in the braille array. In order to enter a letter, press the corresponding patterns. Use 3 to end a sentence, 9 to end a word, and 6 to end a letter.



## Deployment - Online Version

To deploy this code on a server, we tried Google Cloud Platform for their Text-to-Speech api

## Built With

* Espeak - Offline Text to Speech api
* Alsa - Sound Management System
* Raspberry Pi - as the main controller
* Python 2


## Authors

* **Ishan Amlekar** and **Bruce He** 