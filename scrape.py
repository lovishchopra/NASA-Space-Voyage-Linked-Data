import urllib
from bs4 import BeautifulSoup

filterwiki=[]
wikilist=[]

html=urllib.request.urlopen("https://en.wikipedia.org/wiki/List_of_NASA_missions");
soup = BeautifulSoup(html,'html.parser')
#print(soup.prettify())
for link in soup.find_all('a', href=True):
	if(link['href'][:6]=="/wiki/" and link['href'][-4:]!=".jpg"):
		wikilist.append(link['href'][6:])

for x in wikilist: 
	if(x[0:5]=="List_" or x[0:7]=="Special" or x[0:9]=="Wikipedia" or x[0:6]=="Portal" or x[0:8]=="Category" or x[0:4]=="Help"):
		continue
	x=x.replace('\u2013','')
	filterwiki.append(x)

f = open("names.txt", "w")
for x in filterwiki:
	f.write(x+"\n")