import requests
from bs4 import BeautifulSoup


link = "https://login.gitam.edu/Eventlist.aspx"

def getEvents():
    eventList = []
    try:
        html = requests.get(link)
        soup = BeautifulSoup(html.text, 'html.parser')
        events = soup.find_all("div", class_="event_list_block")
        for event in events:
            date = event.find("h6").text
            title = event.find("h3").text
            mode = event.find("h5").text
            branch = event.find_all("h6")[2].text
            eventList.append((title,date,mode,branch))
        return eventList
    except:
        pass

print(getEvents())