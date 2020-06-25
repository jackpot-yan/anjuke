import requests
from bs4 import BeautifulSoup
import time

header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 '
                        'Safari/537.36'}
for i in range(1, 11):
    url = 'https://beijing.anjuke.com/sale/' + str(i)
    r = requests.get(url, headers=header)
    soup = BeautifulSoup(r.text, 'lxml')
    house_list = soup.find_all('li', class_="list-item")
    for house in house_list:
        name = house.find('div', class_='house-title').a.text.strip()
        price = house.find('span', class_='price-det').text.strip()
        price_area = house.find('span', class_='unit-price').text.strip()
        no_room = house.find('div', class_='details-item').span.text
        area = house.find('div', class_='details-item').contents[3].text
        floor = house.find('div', class_='details-item').contents[5].text
        year = house.find('div', class_='details-item').contents[7].text
        broker = house.find('span', class_='brokername').text
        broker = broker[1:]
        address = address.replace('\xa0\xa0\n')
        tag_list = house.find_all('span', class_='item-tags')
        tags = [i.text for i in tag_list]
        print(name, price, price_area, no_room, area, floor, year, broker, address, tags)
        time.sleep(5)
