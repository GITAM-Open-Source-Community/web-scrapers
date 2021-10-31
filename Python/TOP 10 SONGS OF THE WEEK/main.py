import requests

from bs4 import BeautifulSoup

import lxml


response = requests.get("https://genius.com/")

artixt_content = response.text


soup = BeautifulSoup(artixt_content,"lxml")

songs_list = soup.find_all(name="div", class_ = "ChartSongdesktop__Title-sc-18658hh-3 fODYHn")

new_top_list = [ x.getText()  for x in songs_list]


with open("Top10song.txt",mode = "w",encoding="utf-8") as list:
    for x in new_top_list:
        list.write(f"{x} \n")
