from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

htmldata = urlopen('https://www.karavalimunjavu.com/News_date.aspx?dt=2023-08-25')
soup = BeautifulSoup(htmldata, 'html.parser')
images = soup.find_all('img')

for item in images:
	print(item['src'])

