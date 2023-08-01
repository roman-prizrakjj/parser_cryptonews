import requests
from bs4 import BeautifulSoup


def main_page_urls(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    news = soup.findAll("div", class_="row news-item start-xs")
    links = []
    for post in news:
        if post.get("data-title") is not None:
            title = (post.get("data-title"))
        if post.get("data-id") is not None:
            link = ("https://cryptonews.net" + post.get("data-id"))
        links.append([title, link ])
    return links




def multiple_page_urls():
    number = int(input("какое колличество страниц нужно спарсить:"))
    links =[]
    for i in range(1, number+1):
        url = f"https://cryptonews.net/ru/?page={i}"
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        news = soup.findAll("div", class_="row news-item start-xs")

        for post in news:
            if post.get("data-title") is not None:
                title = (post.get("data-title"))
            if post.get("data-id") is not None:
                link = ("https://cryptonews.net" + post.get("data-id"))
            links.append([title, link ])

    return links


