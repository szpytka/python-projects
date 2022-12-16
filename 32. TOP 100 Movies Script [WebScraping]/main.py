from bs4 import BeautifulSoup
import requests
import random

URL = 'https://www.empireonline.com/movies/features/best-movies-2/'


def get_key(val):
    for key, value in result.items():
        if val == value:
            return key


response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, 'html.parser')

articles_title = []
for i in range(100):
    attributes = {
        'data-test': f'listicle-item-{i}',
        'class': 'jsx-3523802742 listicle-item'
    }
    for article in soup.find_all(name='div', attrs=attributes):
        articles_title.append(article.findNext(name='img', alt=True)['alt'])

numbers = [number for number in range(100, 0, -1)]

result = dict(zip(numbers, articles_title))
# print(result)

what_to_watch = random.choice(result)
rating_position = get_key(what_to_watch)

print(f"Movie to watch: \"{what_to_watch}\" at position {rating_position} out of 100."
      f"\nData from EmpireOnline All Time TOP 100 Movies Rating")

with open('movies.txt', mode='w') as file:
    for key, value in result.items():
        file.write(f'{key}) {value}\n')
