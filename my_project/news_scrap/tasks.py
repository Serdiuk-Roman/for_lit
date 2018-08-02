
# pip install requests
# pip install beautifulsoup4

from __future__ import absolute_import, unicode_literals
from celery import shared_task

from bs4 import BeautifulSoup
import requests


@shared_task
def blablabla():

    url = "https://ua.censor.net.ua/news/all"

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    main_block = soup.find(class_="curpane")

    main_list = main_block.find_all(
        'article',
        {"class": "item"},
    )

    first_el = [
        {
            "title": el.find("h3").text,
            "time": el.find("time").get("datetime"),
            "link": el.find("a").get("href"),
            "short_text": el.find("div", {"class": "anounce"}).find("a").text,
        }
        for el in main_list
    ]

    return first_el
