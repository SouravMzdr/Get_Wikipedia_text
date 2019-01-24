from bs4 import BeautifulSoup
from requests import get
import os
import io

#Setting up the url
search=input("Enter Wikipedia search term:")
search=search.capitalize()
search=search.replace(" ","_")

url="http://www.wikipedia.org/wiki/"+search
htmlString =get(url).text

#Check for Error 404
if get(url).status_code == 404:
    print("Page not found!!")
    print("Please check whether your search term is spelled correctly and whether a wiki page exist for the searched topic")
    os.system('pause')

#Parsing the soup
html=BeautifulSoup(htmlString,'lxml')

entries = html.find('div', id="content")
entries = entries.find_all(['h1','h2', 'p'])
text = [e.get_text() for e in entries]

# Put the extracted text into seperate txt file
search=search.replace("_"," ")
path=search+".txt"

with io.open(path, "w+", encoding="utf-8") as f:
    for t in text:
        f.write(t + "\n")
