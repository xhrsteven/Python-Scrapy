from urllib.request import urlopen
from bs4 import BeautifulSoup
from requests import HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),features="lxml")
        title = bsObj.h1
    except AttributeError as e:
        return None

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)

    
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,features="lxml")
nameList = bsObj.findAll("span",{"class": "green"})
for name in nameList:
    print(name.get_text())

allText = bsObj.findAll(id = "text")
print(allText[0].get_text())
