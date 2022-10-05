import bs4
import requests
from fake_headers import Headers


URL ='https://habr.com'
headers = Headers(os="win", headers=True).generate()
response = requests.get(URL+'/ru/all/', headers= headers)
html = response.text

KEYWORDS = ['Фриланс', 'Физика', 'web', 'python', 'Облако', 'Блог','IT-инфраструктура', 'DevOps', 'Софт', 'PostgreSQL']

soup = bs4.BeautifulSoup(html, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')

for article in articles:
    previews = [art.span.text for art in article.find_all('span', class_='tm-article-snippet__hubs-item')]
    date = article.time.text
    title = article.find('a', class_='tm-article-snippet__title-link')
    href = title['href']
    span_title = title.text


    for prev in previews:
        if prev in KEYWORDS:
            result = f'дата {date}\nЗаголовок {span_title}\nСылка {URL}{href}\n'
            print(result)
