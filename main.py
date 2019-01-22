from bs4 import BeautifulSoup
from requests import get

search=input("Enter search term")
url="http://www.wikipedia.org/wiki/"+search
htmlString =get(url).text
html=BeautifulSoup(htmlString,'lxml')
entries=html.find_all('div', {"class":"mw-parser-output"})
text=[e.get_text() for e in entries]
print(text)

path=search+".txt"
f=open(path,"w")
f.writelines(text[0])


