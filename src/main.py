# This is a script for testing python, whether it is able to read files

import os
import bs4
from time import sleep

from config import config
from writeInHTML import writeInHTML


def main():
    tupel = config()
    media = tupel[0]
    Tts = tupel[1]

    while True:
        for element in media:
            writeInHTML(element)
            sleep(Tts)


    
if __name__ == "__main__":
    main()