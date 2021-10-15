from bs4 import BeautifulSoup
import requests
import sys

baseUrl = "https://github.com/topics/"+sys.argv[1]

res = requests.get(baseUrl)
soup = BeautifulSoup(res.text, 'lxml')

repos = soup.find_all('h3', {'class': 'f3 color-text-secondary text-normal lh-condensed'})

#Default Descending order
'''for repo in repos:
    print("https://github.com" + repo.find_all('a')[1]['href'])
'''
    
#For Ascending Order(Starting with the least number of stars and save the list in a text file)

textfile = open("github_topics.txt", "w")
for repo in reversed(repos):
    print("https://github.com" + repo.find_all('a')[1]['href'])
    textfile.write(repo + "\n")

textfile.close()
