from bs4 import BeautifulSoup, SoupStrainer
import requests
from pprint import pprint

inputFields = SoupStrainer('input')

baseURL = 'https://news.google.com'
response = requests.get(baseURL+'/topstories?hl=en-IN&gl=IN&ceid=IN:en')

soup = BeautifulSoup(response.text, 'lxml')
headlines = soup.find_all('h3', {'class': 'ipQwMb ekueJc RD0gLb'})

for headline in headlines:
    obj = {'headline': headline.text, 'readHere': (baseURL+(headline.find_previous_sibling('a').attrs['href'][1:]))}
    pprint(obj)
    print('\n')