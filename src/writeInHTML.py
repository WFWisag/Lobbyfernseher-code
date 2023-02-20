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


def writeInHTML(element):
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)

    if getFileType(element) == "img":
        imgTags = str(soup.img)
        print(imgTags)

        newhtmlfileRT = strSoup.replace(
            imgTags, f"<img class='folie' src='media/{element}' />")

        with open("index.html", "w+") as newhtmlfile:
            newhtmlfile.write(newhtmlfileRT)
    elif getFileType(element) == "vid":
        vidTags = str(soup.video)
        print(vidTags)

        clipDuration = getVideoDuration(element)
        TimeControl = str(soup.find("meta", {"https-equiv": "refresh"}))
        newhtmlfileRT = strSoup.replace(
            TimeControl, f"<meta http-equiv='refresh' content='{clipDuration}'>")

        newhtmlfileRT = strSoup.replace(
            vidTags, f"<video class='folie' src='media/{element}' autoplay></video>")

        with open("index.html", "w+") as newhtmlfile:
            newhtmlfile.write(newhtmlfileRT)
