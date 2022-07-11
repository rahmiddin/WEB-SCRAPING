import bs4
import requests
from fake_headers import Headers

URL = 'https://habr.com/ru/all/'
KEYWORDS = {'дизайн', 'фото', 'web', 'Python'}

header = Headers(
        headers=True  # generate misc headers
    )


HEADER = header.generate()


RESPONSE = requests.get(url='https://habr.com/ru/all/', headers=HEADER)
TEXT = RESPONSE.text


soup = bs4.BeautifulSoup(TEXT, features='html.parser')
articles = soup.findAll('article')


for article in articles:
    hubs = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
    hubs = set([hub.find('span') for hub in hubs])
    date = article.find('time')['datetime']
    title = article.find('h2').find('a').find('span').text
    link = 'http://habr.com' + article.find('h2').find('a')['href']
    for hub in hubs:
        if hub.text in KEYWORDS:
            print(f'{date},{title},{link}')
