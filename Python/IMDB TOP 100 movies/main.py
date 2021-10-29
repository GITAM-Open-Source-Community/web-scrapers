from bs4 import BeautifulSoup
import requests
import lxml


response = requests.get("https://www.rottentomatoes.com/top/bestofrt/")

content = response.text

soup = BeautifulSoup(content,"lxml")

list = soup.select(selector="tr a ")


text = [ x.getText().replace("\n","") for x in list]



with open("movielist.txt", mode="w") as movie:
    for x in text:
        movie.write(f"{x} \n")
