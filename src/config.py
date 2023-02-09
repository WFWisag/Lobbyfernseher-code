# Config-Script for config the diashow

import os
import bs4

def getDir() -> tuple:
    os.chdir(os.getcwd())

    imgDir = os.listdir(r"src/img")
    vidDir = os.listdir(r"src/vid")
    return imgDir, vidDir

def config() -> tuple:
    os.chdir(os.getcwd())

    media = getDir()[0] + getDir()[1]

    while True:
        try:
            Tts = int(input("Umschaltzeit (in s): "))

            if Tts <= 0:
                raise ValueError
            else:
                pass
        except ValueError:
            continue

        break

    with open("src/index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
        print(strSoup)

        newTimeControl = strSoup.replace("<meta http-equiv='refresh' content='30'>", f"<meta http-equiv='refresh' content='{Tts}'")
        print(newTimeControl)

        htmlfile.write(newTimeControl)

    return media, Tts

    


if __name__ == "__main__":
    config()