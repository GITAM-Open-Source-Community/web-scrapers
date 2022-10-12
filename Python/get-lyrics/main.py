from bs4 import BeautifulSoup
import requests


def getLyrics(title):
    headers = {
        "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36"
    }
    session = requests.Session()
    res = session.get("https://www.musixmatch.com/search/"+title, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    link = soup.find(class_ = "title").attrs["href"]
    res = session.get('https://www.musixmatch.com/'+link, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    lyrics=""
    for i in soup.find_all(class_ = "lyrics__content__ok"):
        lyrics += i.text+'\n'
    return lyrics


song = input("Enter the name of song: ")

try:
    lyrics = getLyrics(song)
    print(f"======== {song} ======== \n")
    print(lyrics)
except:
    print("Something went wrong please check the name and try again.")