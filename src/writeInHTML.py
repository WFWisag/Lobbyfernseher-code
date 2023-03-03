import bs4
from moviepy.editor import VideoFileClip as vfc
import math
import os 


def getFileType(element) -> str:
    if element.endswith(".png") or element.endswith(".jpg") or element.endswith(".jpeg") or element.endswith(".gif"):
        return "img"
    elif element.endswith(".mp4"):
        return "vid"
    else:
        return "error"


def getVideoDuration(element) -> int:
    clip = vfc(element)
    duration = math.ceil(clip.duration)
    return int(duration)


def getReplacedTag() -> tuple:
    os.chdir(os.getcwd())
    # it should either return the img or video tag
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')

        if soup.img == None:
            return str(soup.video), "vid"
        elif soup.video == None:
            return str(soup.img), "img"
        else:
            return "error"


def writeTimeControlInHTML(Tts):
    os.chdir(os.getcwd())
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    TimeControl = str(soup.find_all("meta")[1])
    NewTimeControl = f"<meta content='{Tts}' http-equiv='refresh'>"

    newhtmlfile = strSoup.replace(TimeControl, NewTimeControl)

    with open("index.html", "w+") as htmlfile:
        htmlfile.write(newhtmlfile)


def writeIMGinHTML(element, replacedTag):
    os.chdir(os.getcwd())
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    newhtmlfileRT = strSoup.replace(
        replacedTag, f"<img class='folie' src='media/{element}' />")

    with open("index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)


def writeVIDinHTML(element, replacedTag):
    os.chdir(os.getcwd())
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    clipDuration = getVideoDuration(element)
    writeTimeControlInHTML(clipDuration)

    newhtmlfileRT = strSoup.replace(
        replacedTag, f"<video class='folie' src='media/{element}' autoplay></video>")

    with open("index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)


def writeInHTML(element):
    rT = getReplacedTag()[0]
    rTT = getReplacedTag()[1]

    if rTT == "img":
        writeIMGinHTML(element, rT)
    elif rTT == "vid":
        writeVIDinHTML(element, rT)
