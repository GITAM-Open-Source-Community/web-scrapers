import requests
from bs4 import BeautifulSoup


def get_restaurant_details():
    url = "https://www.zomato.com/rasoigharuae/info"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:76.0) Gecko/20100101 Firefox/76.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    # print(soup.prettify())
    loc = soup.find("a", {"class": "sc-iGrrsa dEjBWV"}).text  # location
    cuisine_list = (soup.find_all("a", {"class": "sc-bMvGRv jMWyZs"}))  # cuisine
    dining_review = soup.find_all("div", {"class": "sc-1q7bklc-1 cILgox"})[0]  # dining reviews
    delivery_review = soup.find_all("div", {"class": "sc-1q7bklc-1 cILgox"})[1]  # delivery reviews

    print("Location: ", loc)
    print("Cuisines: ")
    for res in cuisine_list:
        print(res.text)
    for res in dining_review:
        print("Dining Review: ", res.text)
    for res in delivery_review:
        print("Delivery Review: ", res.text)


if __name__ == "__main__":
    get_restaurant_details()
