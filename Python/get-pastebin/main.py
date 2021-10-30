import re, requests
from bs4 import BeautifulSoup

long_max = 8
long_min = 8
char_null = ['']
chars_min = ['a','b','c', 'd','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
chars_may = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
chars_num = ['0','1','2','3','4','5','6','7','8','9']
chars_spe = ['.','-','_','/','@']
allows = []
allows += char_null
allows += chars_min
allows += chars_num
total_chars = len(allows)
char_n_max = total_chars - 1
list1 = []
list_max = []

for chars in range(0, long_max): list1 += [0]
for i in range(1, long_min + 1): list1[-(i)] = 1
for chars in range(0, long_max): list_max += [total_chars - 1]

def toKey(cadena1):
    password = ""
    for index in cadena1: password += allows[index]
    return password

def isMax(cadena1):
    if toKey(cadena1) != toKey(list_max): return False
    return True


def upList(cadena1):
    unit = 1
    counter = 0
    for dig in range(1, long_max + 1):
        if list1[-(dig)] < char_n_max:
            if unit == 1:
                list1[-(dig)] += 1
                unit = 0
            return cadena1
        elif counter == 1:
            list1[-(dig)] += 1
            counter = 0
            return cadena1
        else:
            list1[-(dig)] = 1
            counter = 1
            return cadena1

if __name__ == '__main__':
    url_base = "https://pastebin.com/"
    while True:
        password = toKey(list1)
        url = url_base + password
        try:
            response = requests.get(url)
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            data = soup.find("div", {"id": "selectable"})
            if data:
                data = str(re.compile(r'<[^>]+>').sub('', data))
                info_user = soup.find("div", {"class": "paste_box_line2"}).text.split("\n")
                dict_paste = {"url": url, "user": info_user[1].strip(), "date": info_user[2].strip(), "data": data}
                print("URL download - " + str(url))
            else: print("URL does not exist or it was deleted - " + str(url))
        except: print('ERROR in '+str(url))
        if isMax(list1): break
        list1 = upList(list1)
