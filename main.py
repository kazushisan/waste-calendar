# import os
import arrow
from datetime import datetime
from bs4 import BeautifulSoup
import urllib.request
import re
from ics import Calendar, Event

regex = re.compile(r"^\/images\/([0-9]{1,2}).*\.png$")

c = Calendar()

year = 2019
month = 4
day_before = 0

while (True):
    url = f"https://www.53cal.jp/areacalendar?city=1080104&area=1080104102&yy={year}&mm={month}"
    html = urllib.request.urlopen(url)
    soup = BeautifulSoup(html, "html.parser")
    cells = soup.select('td')
    for cell in cells:
        if len(cell.select('#cal_kind')) == 0:
            continue
        src = cell.select('img')[0]['src'].strip()
        day = int(re.sub(regex, r'\1', src))

        if (day_before == day):
            continue
        else:
            day_before = day

        e = Event()
        e.name = cell.select('a')[0]['title'].replace('\n', ' ').strip()
        e.begin = (datetime(year, month, day, 8, 0), 'Asia/Tokyo')
        e.end = e.begin
        c.events.add(e)
    if month == 3 and year == 2020:
        break
    if month == 12:
        year += 1
        month = 1
    else:
        month += 1

with open('waste.ics', 'w') as waste_file:
    waste_file.writelines(c)
