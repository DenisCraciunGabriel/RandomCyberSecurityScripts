#!/usr/bin/env python3


import requests
from bs4 import BeautifulSoup

html= requests.get("http://10.10.31.88/3/")

soup = BeautifulSoup(html.text, "lxml")

links = soup.find_all("a", href=True)

for link in links:
	print(link)
