# Config-Script for config the diashow

import os
from src.writeInHTML import writeTimeControlInHTML as wtc

os.chdir(os.getcwd())

def getDir() -> list:
    media = os.listdir("media/")
    return media


def readconfigFile() -> int:  # TODO: change the return type to tuple, when more config options are available
    os.chdir(os.getcwd())

    with open("config.txt", "r+") as configfile:
        config = configfile.readlines()

        try:
            Tts = int()
            for line in config:
                if line.startswith("Tts"):
                    Tts = int(line.split("=")[1])
                else:
                    pass
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
    Tts = readconfigFile()

    wtc(Tts)

    return sorted(media), Tts


if __name__ == "__main__":
    config()
