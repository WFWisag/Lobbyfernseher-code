# This is a script for testing python, whether it is able to read files

import os
import bs4

os.chdir(os.getcwd())

def getDir() -> list:
    imgDir = os.listdir(r"src/img")
    return imgDir

def writeInHTML():
    imgDir = getDir()

    htmlfile = open("src/index.html", "r")
    soup = bs4.BeautifulSoup(htmlfile, 'html.parser')

    imgTag = soup.img.attrs["id"] = "test"
    print(imgTag)

    
if __name__ == "__main__":
    writeInHTML()