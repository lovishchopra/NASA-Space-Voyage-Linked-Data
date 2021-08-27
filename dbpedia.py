from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from difflib import get_close_matches

import urllib
from bs4 import BeautifulSoup

import time

driver = webdriver.Chrome()
driver.get("http://dbpedia.org/snorql/?query=SELECT++DISTINCT+%3Fs+WHERE+%7B%0D%0A+++%3Fs+%3Fp+%3Fo.%0D%0A+++%3Fs+rdf%3Atype+%3Chttp%3A%2F%2Fdbpedia.org%2Fontology%2FSatellite%3E.%0D%0A+++%3Fs+dbp%3Aoperator+dbr%3ANASA.%0D%0A+++FILTER%28LANG%28%3Fo%29%3D%22en%22%29.%0D%0A%7D%0D%0A")
time.sleep(5);
html = driver.page_source
soup = BeautifulSoup(html,'html.parser')
tl=soup.find_all(attrs={"class" : "uri"})
allmission=[]

for x in tl:
	children = x.findChildren("a" , recursive=False)[0]
	allmission.append(children.text)

print(allmission,len(allmission))