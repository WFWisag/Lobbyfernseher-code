# This is a script for testing python, whether it is able to read files

import os
import bs4
from time import sleep

from config import config

os.chdir(os.getcwd())



def writeInHTML(element):
    with open("src/index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
    
    imgTags = str(soup.img)
    print(imgTags)

    newhtmlfileRT = strSoup.replace(imgTags, f"<img class='folie' src='media/{element}' />")

    with open("src/index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)

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