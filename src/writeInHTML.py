import bs4

def writeInHTML(element):
    with open("index.html", "r+") as htmlfile:
        soup = bs4.BeautifulSoup(htmlfile, 'html.parser')
        strSoup = str(soup)
    
    imgTags = str(soup.img)
    print(imgTags)

    newhtmlfileRT = strSoup.replace(imgTags, f"<img class='folie' src='media/{element}' />")

    with open("index.html", "w+") as newhtmlfile:
        newhtmlfile.write(newhtmlfileRT)
