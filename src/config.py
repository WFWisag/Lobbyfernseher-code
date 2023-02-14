# Config-Script for config the diashow

import os
import bs4

def getDir() -> list:
    os.chdir(os.getcwd())

    media = os.listdir(r"d:/Praktikum/Raspberry Pi für Lobbyfernseher/code/src/media")
    return media

def readconfigFile() -> float: # TODO: change the return type to tuple, when more config options are available
    os.chdir(os.getcwd())

    with open("d:/Praktikum/Raspberry Pi für Lobbyfernseher/code/src/config.txt", "r+") as configfile:
        config = configfile.readlines()
        
        try:
            Tts = float(config[1].strip("Tts: "))
            if Tts <= 0:
                raise ValueError
            else:
                pass
        except ValueError:
            print("Umschaltzeit muss größer als 0 sein!")
            exit(1)

    return Tts

def config() -> tuple:
    os.chdir(os.getcwd())

    media = getDir()
    Tts = readconfigFile() # TODO: change the return type to tuple, when more config options are available

    with open("d:/Praktikum/Raspberry Pi für Lobbyfernseher/code/src/index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
        
        TimeControl = str(soup.find_all("meta")[1])
        NewTimeControl = f"<meta content='{Tts}' http-equiv='refresh'>"

        newhtmlfile = strSoup.replace(TimeControl, NewTimeControl)

    with open("d:/Praktikum/Raspberry Pi für Lobbyfernseher/code/src/index.html", "w+") as htmlfile:
        htmlfile.write(newhtmlfile)

    return sorted(media), Tts

    


if __name__ == "__main__":
    config()