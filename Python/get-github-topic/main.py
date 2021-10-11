from bs4 import BeautifulSoup
import requests
import sys

baseUrl = "https://github.com/topics/"+sys.argv[1]

res = requests.get(baseUrl)
soup = BeautifulSoup(res.text, 'lxml')

repos = soup.find_all('h3', {'class': 'f3 color-text-secondary text-normal lh-condensed'})

for repo in repos:
    print("https://github.com" + repo.find_all('a')[1]['href'])