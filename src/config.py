# Config-Script for config the diashow

import os
import bs4

def getDir() -> list:
    os.chdir(os.getcwd())

    media = os.listdir(r"d:\Praktikum\Raspberry Pi für Lobbyfernseher\code\src/media")
    return media

def config() -> tuple:
    os.chdir(os.getcwd())

    media = getDir()

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

    with open(r"d:\Praktikum\Raspberry Pi für Lobbyfernseher\code\src/index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
        
        TimeControl = str(soup.find_all("meta")[1])
        NewTimeControl = f"<meta content='{Tts}' http-equiv='refresh'>"

        newhtmlfile = strSoup.replace(TimeControl, NewTimeControl)

    with open(r"d:\Praktikum\Raspberry Pi für Lobbyfernseher\code\src/index.html", "w+") as htmlfile:
        htmlfile.write(newhtmlfile)

    return sorted(media), Tts

    


if __name__ == "__main__":
    config()