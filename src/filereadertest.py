# test

from bs4 import BeautifulSoup as BS


with open("src/index.html", "r+") as htmlfile:
        soup = BS(htmlfile, 'html.parser')
        strSoup = str(soup)
        
        TimeControl = soup.find_all("meta")[1]

        NewTimeControl = ()
        