# Brailliant

Real-time Braille to Speech Converter - To allow blind and deaf people to live a more accesible life!

### Prerequisites

* Raspberry Pi booted on Raspbian OS
* Espeak
* Alsa
* An IDE for Python 2


### Installation

A step by step series of examples that tell you how to get a development env running


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

Explain how to run the automated tests for this system


## Deployment - Online Version

To deploy this code on a server, we tried Google Cloud Platform for their Text-to-Speech api

## Built With

* Espeak - Offline Text to Speech api
* Alsa - Sound Management System
* Raspberry Pi - as the main controller
* Python 2


## Authors

* **Ishan Amlekar** and **Bruce He** 