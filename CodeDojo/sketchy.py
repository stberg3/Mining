# sketchy.py

import lxml
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import FancyURLopener

class MeinOpener(FancyURLopener):
    version = "Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) \
 Gecko/20071127 Firefox/2.0.0.11"

mo = MeinOpener()
url = "http://www.thedailybeast.com/cheat-sheet.html"
# url = "http://www.thedailybeast.com/cheats/2017/01/23/report-michael-flynn-under-investigation-for-russia-ties.html?via=desktop&source=copyurl"
html = mo.open(url).read()
soup = BeautifulSoup(html, "lxml")
# print(soup.prettify().encode("utf-8")[0:1000])
paras = soup.find_all('p')
headings = soup.find_all("h1", class_="CheatHeader__title")
imgs = soup.find_all(class_="CheatHeader__image")
index = 0
# for p in paras:
#     print(p.encode("utf-8"))
#     print("----------------------")

news = open("test.html", "w")
doc = "<!DOCTYPE html>\n"
doc += "<html>"
doc += "<head>"
doc += "<style>"
doc += "img { width: 25%; height: 25%}"
doc += "</style>"
doc += "<title>Test Scrape</title>"
doc += "</head>"
doc += "<body>"
for p in paras:
    doc += str(headings[index])
    doc += str(imgs[index].figure)
    doc+=str(p)
    doc+= ("<hr>")
    index += 1
doc += "</body>"
doc += "</html>"

news.write(doc)
