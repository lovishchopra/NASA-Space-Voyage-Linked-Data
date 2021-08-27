import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from difflib import get_close_matches

import urllib
from bs4 import BeautifulSoup
import re

def RegexFilter(strFilter):
    n = len(strFilter)
    newstr=""
    i = 0
    while(i<n):
        if(strFilter[i]=='['):
            while(strFilter[i]!=']'):
                i+=1
        if(i<n and strFilter[i]!=']'):
            newstr+=strFilter[i]
        i+=1
    newstr=newstr.rstrip("\n\r ").lstrip("\n\r ")
    return newstr


def FetchData(totoken):
	html=urllib.request.urlopen("https://en.wikipedia.org/wiki/"+totoken);
	soup = BeautifulSoup(html,'html.parser')
	para = soup.find_all('p')
	for p in para:
		f=p.text.rstrip("\n\r ").lstrip("\n\r ")
		if f!="":
			print(f)
			return RegexFilter(f)
	return ""

file1="output1.csv"
inp=[]
out=[]

with open(file1,'r') as f1:
    csvreader=csv.reader(f1,delimiter=';')
    for row in csvreader:
        inp.append(row)

inp[0].append("description")

for row in inp[1:]:
    description=FetchData(row[0])
    row.append(description)
    out.append(row)

with open("finaloutput.csv", "w") as f:
    writer = csv.writer(f,delimiter=';')
    writer.writerows(out)