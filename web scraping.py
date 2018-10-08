from bs4 import BeautifulSoup

import requests
r= requests.get("http://www.pythonforbeginners.com")

data = r.text

#print(data)

soup = BeautifulSoup(data,"html.parser")

#print(soup.find_all('a'))

for link in soup.find_all('a'):
    print(link.get('href'))