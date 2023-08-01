from utils.url import *


def main_page_article(url):
    articles = []
    count = 1
    for url in main_page_urls(url):
        res = requests.get(url[1])
        soup = BeautifulSoup(res.text, "html.parser")
        post = soup.find("div", class_="cn-content").text
        clean_post = post.replace("\n", " ")
        image_link = soup.find("div", class_="news-item detail content_text").get("data-image")
        articles.append([clean_post])
        with open("article.txt", "a", encoding='utf-8') as file:
            file.writelines(f"СТАТЬЯ №{count} \nФотка :{image_link} \n{clean_post}\n")
        count += 1
    return articles



def multiple_pages_article():
    articles = []
    count = 1
    for url in multiple_page_urls():
        res = requests.get(url[1])
        soup = BeautifulSoup(res.text, "html.parser")
        post = soup.find("div", class_="cn-content").text
        clean_post = post.replace("\n", " ")
        image_link = soup.find("div", class_="news-item detail content_text").get("data-image")
        articles.append([image_link, clean_post])
        with open("article.txt", "a", encoding='utf-8') as file:
            file.writelines(f"СТАТЬЯ №{count} \nФотка :{image_link} \n{clean_post}\n")
        count += 1
    return articles
