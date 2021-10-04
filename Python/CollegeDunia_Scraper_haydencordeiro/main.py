import json
from bs4 import BeautifulSoup
import pandas as pd
import requests

link = "https://collegedunia.com/btech/maharashtra-colleges?sub_stream_id=424,426"
user_agent = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0'
    }
session = requests.Session()
collegeList = []

html = session.get(link, headers=user_agent).text
soup = BeautifulSoup(html,'html.parser')
results = soup.find_all("script", {"type" : "application/ld+json"})
script = results[3]
jsonData = json.loads(script.string)
list = jsonData["itemListElement"]
for i in list:
    html2 = session.get(i['url'], headers=user_agent).text
    soup2 = BeautifulSoup(html2,'html.parser')
    results2 = soup2.find_all("script", {"type" : "application/ld+json"})
    script2 = results2[2]
    jsonData2 = json.loads(script2.string)
    collegeName = jsonData2["name"]
    collegeList.append(collegeName)

print(collegeList)

df = pd.DataFrame({'College List':collegeList})
df.to_excel ('export_dataframe.xlsx', index = True, header=True)