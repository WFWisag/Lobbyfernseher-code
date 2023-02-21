import bs4
from moviepy.editor import VideoFileClip as vfc
import math


def getFileType(element):
    if element.endswith(".png") or element.endswith(".jpg") or element.endswith(".jpeg") or element.endswith(".gif"):
        return "img"
    elif element.endswith(".mp4"):
        return "vid"
    else:
        return "error"


def getVideoDuration(element) -> int:
    clip = vfc(element)
    duration = clip.duration.ceil()
    return int(duration)


def getReplacedTag():
    # it should either return the img or video tag
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')

        if soup.img == None:
            return "vid"
        elif soup.video == None:
            return "img"
        else:
            return "error"


def writeTimeControlInHTML(Tts):
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    TimeControl = str(soup.find_all("meta")[1])
    NewTimeControl = f"<meta content='{Tts}' http-equiv='refresh'>"

    newhtmlfile = strSoup.replace(TimeControl, NewTimeControl)

    with open("index.html", "w+") as htmlfile:
        htmlfile.write(newhtmlfile)


def writeIMGinHTML(element):
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    if getReplacedTag() == "vid":
        oldTags = str(soup.video)
    elif getReplacedTag() == "img":
        oldTags = str(soup.img)
    else:
        exit(-1)

    newhtmlfileRT = strSoup.replace(
        oldTags, f"<img class='folie' src='media/{element}' />")

    with open("index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)


def writeVIDinHTML(element):
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    if getReplacedTag() == "vid":
        oldTags = str(soup.video)
    elif getReplacedTag() == "img":
        oldTags = str(soup.img)
    else:
        exit(-1)

    clipDuration = getVideoDuration(element)
    writeTimeControlInHTML(clipDuration)

    newhtmlfileRT = strSoup.replace(
        oldTags, f"<video class='folie' src='media/{element}' autoplay></video>")

    with open("index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)


def writeInHTML(element):
    if getFileType(element) == "img":
        writeIMGinHTML(element)
    elif getFileType(element) == "vid":
        writeVIDinHTML(element)
