
import requests
import lxml.html as html
import json


def get_page(url):
    req = requests.get(url)
    page = html.fromstring(req.content)
    return page


def get_post_link(page):
    article_link = page.xpath(
        '//a[@class="post__title_link"]/@href'
    )
    return article_link


def get_data(page):
    res = {}

    res["title"] = page.xpath('//span[@class="post__title-text"]/text()')

    res["text"] = page.xpath(
        '//div[contains(@class, "post__body_full")]/div/descendant::text()')
    res["text"] = [x.strip() for x in res["text"]]
    res["text"] = [x for x in res["text"] if x]

    res["img"] = page.xpath(
        '//div[contains(@class, "post__body_full")]/div//img/@src')

    return res


def main():

    data = []

    main_domain_start = "https://habr.com/"
    main_page = get_page(main_domain_start)
    links = get_post_link(main_page)

    for link in links:
        page_data = (get_data(get_page(link)))
        data.append(page_data)

    with open("data.json", 'w', encoding="utf-8") as f:
        json.dump(data, f, sort_keys=True, indent=4, ensure_ascii=False)


main()
