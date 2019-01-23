from bs4 import BeautifulSoup
from requests import get

#Setting up the url
search=input("Enter search term:")
search=search.capitalize()
search=search.replace(" ","_")

url="http://www.wikipedia.org/wiki/"+search
htmlString =get(url).text

#Parsing the soup
html=BeautifulSoup(htmlString,'lxml')
entries = html.find('div', id="content")
entries = entries.find_all(['h1','h2', 'p'])
text = [e.get_text() for e in entries]

# Put the extracted text into seperate txt file
search=search.replace("_"," ")
path=search+".txt"

f=open(path,"w+")
for t in text:
    f.write(t+"\n")

