#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'}
payload = {'email':'','form_id':'packt_user_login_form','password':''}
url = 'https://www.packtpub.com/'

session = requests.Session()
req = session.get(url, headers=headers)

req = session.post(url,headers=headers,data=payload)

req = requests.get('https://www.packtpub.com/packt/offers/free-learning', headers=headers)
soup = BeautifulSoup(req.text,'html.parser')
link = soup.find("a", class_="twelve-days-claim").get('href')


url = 'https://www.packtpub.com/'+link

session.get(url,headers=headers)
