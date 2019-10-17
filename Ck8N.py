import requests
from bs4 import BeautifulSoup

url = 'https://bbc.com/news/world/'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

titles = soup.find_all('h3', class_='gs-c-promo-heading__title gel-pica-bold nw-o-link-split__text')

print(titles)
