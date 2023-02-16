# This is a script for testing python, whether it is able to read files

import os
import bs4
from time import sleep
import RPi.GPIO as GPIO

from config import config
from writeInHTML import writeInHTML


def main():
    tupel = config()
    media = tupel[0]
    Tts = tupel[1]
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18, GPIO.OUT)
    GPIO.output(18, True)

    while True:
        for element in media:
            GPIO.output(18, True)
            writeInHTML(element)
            sleep(Tts)
            GPIO.output(18, False)


    
if __name__ == "__main__":
    main()