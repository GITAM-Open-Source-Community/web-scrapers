from bs4 import BeautifulSoup
import requests

baseUrl = "https://github.com/trending"

res = requests.get(baseUrl)
soup = BeautifulSoup(res.text, 'lxml')

repos = soup.find_all('h1', {'class': 'h3 lh-condensed'})

for repo in repos:
    print("https://github.com/" + repo.find('a')['href'])
