# This is a script for testing python, whether it is able to read files

import os
import bs4

import config

os.chdir(os.getcwd())



def writeInHTML(element):
    with open("src/index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
    
    imgTags = str(soup.img)
    print(imgTags)

    newhtmlfileRT = strSoup.replace(imgTags, f"<img class='folie' src='img/{imgDir[0]}' />")

    with open("src/index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)

def main():
    pass
    
if __name__ == "__main__":
    print()
    #writeInHTML()