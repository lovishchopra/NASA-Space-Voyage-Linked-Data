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

def RegexFilter(strfilter):
    strfilter = strfilter.split(" ")
    n = len(strfilter)
    newstr=""
    for i in range(n):
        mytoken=""
        temp = strfilter[i]
        l = len(temp)
        j = 0
        while(j<l):
            if(temp[j]=='['):
                while(temp[j]!=']'):
                    j+=1
            else:
                mytoken+=temp[j]
            j+=1
        newstr+=mytoken
        newstr+=" "
    return newstr

def FetchData(totoken):
    result = {}
    exceptional_row_count = 0
    html=urllib.request.urlopen("https://en.wikipedia.org/wiki/"+totoken);
    soup = BeautifulSoup(html,'html.parser')
    #print(soup.prettify())
    table = soup.find_all('tbody')[0]
    for tr in table.find_all('tr'):
        if tr.find('th'):
            #print(tr.find('th').prettify())
            #print(tr.find('td').prettify())
            try:
            	result[tr.find('th').text] = tr.find('td').text
            except:
            	print("Missed the row : "+tr.find('th').text)
        else:
            # the first row Logos fall here
            exceptional_row_count += 1

    if exceptional_row_count > 1:
    	print()
        #print( 'WARNING ExceptionalRow>1: ', table)

    filterresult={}
    for x in result.keys():
        try:
            filterresult[x]=RegexFilter(result[x])
        except:
            print(result[x])

    return filterresult

totoken="Apollo_17"
xx=FetchData(totoken)

for x in xx.keys():
    print(x," : ",xx[x]);
