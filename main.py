# import os
# import datetime
from bs4 import BeautifulSoup
import urllib.request
import re

url = "https://www.53cal.jp/areacalendar?city=1080104&area=1080104102&yy=2019&mm=4"
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, "html.parser")

cells = soup.select('td')

regex = re.compile(r"^\/images\/([0-9]{1,2}).*\.png$")

for cell in cells:
	if len(cell.select('#cal_kind')) == 0:
		continue
	src = cell.select('img')[0]['src'].strip()
	day = re.sub(regex, r'\1', src)
	title = cell.select('#cal_kind')[0].text.strip()
	print(day + ' ' + title)