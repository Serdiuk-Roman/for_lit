
# pip install requests
# pip install beautifulsoup4


from bs4 import BeautifulSoup

import requests

url = "http://dataquestio.github.io/web-scraping-pages/simple.html"

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')

main_list = soup.get('article', class_="feed", id="feed")

blocks = main_list.find_all('section', class_='feed__section')

print(blocks)
