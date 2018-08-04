# http://www.learnpython.us/scrapy-vs-selenium-vs-beautifulsoup-vs-requests-vs-lxml-tutorial.html

# import lxml.html as html
# from urllib.request import urlopen
# main_domain_start = "https://habr.com/"
# page = html.parse(urlopen(main_domain_start)).getroot()
# print(page)

# article_links_text = page.xpath(
#     '//li/article[contains(@class, "post")]/h2[@class="post__title"]/a[@class="post__title_link"]/text()'
# )
# article_links = page.xpath(
#     '//li/article[contains(@class, "post")]/h2[@class="post__title"]/a[@class="post__title_link"]/@href'
# )
# print(article_links)


# import requests
# import lxml.html as html

# main_domain_start = "https://habr.com/"

# req = requests.get(main_domain_start)

# page = html.fromstring(req.content)

# article_body = page.xpath(
#     '//li/article[contains(@class, "post")]/div[contains(@class, "post__body")]'
# )

# article_text = [
#     el.xpath('.//text()')
#     for el in article_body
# ]

# for i in article_text:
#     print("######################################################################")
#     print(i)


import requests
from bs4 import BeautifulSoup

main_domain_start = "https://habr.com/"
req = requests.get(main_domain_start)

soup = BeautifulSoup(req.content, 'html.parser')

article_header = soup.select('li article.post h2 a')

for i in article_header:
    print(i.get('href'))







x2 = response.xpath('//ul[@id="comments-list"]/li')
y2 = [
    {el.xpath(
        './/div[contains(@class, "comment")]/div[contains(@class, "comment__head")]/a/span[contains(@class, "user-info__nickname")]/text()').extract():
    el.xpath(
        './/div[contains(@class, "comment")]/div[contains(@class, "comment__head")]
        )}
for el in x2]
