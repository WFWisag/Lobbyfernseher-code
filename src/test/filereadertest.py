# test

from bs4 import BeautifulSoup as BS


with open("src/index.html", "r+") as htmlfile:
        soup = BS(htmlfile, 'html.parser')
        strSoup = str(soup)

        tts = int(input("ZEIT"))
        
        TimeControl = str(soup.find_all("meta")[1])

        NewTimeControl = f"<meta content='{tts}' http-equiv='refresh'>"

        newhtmlfile = strSoup.replace(TimeControl, NewTimeControl)

with open("src/index.html", "w+") as htmlfile:
        htmlfile.write(newhtmlfile)