import time

from utils.article import *
from utils.config import *




flag = input("""
1 = Получить статьи с главной страницы
2 = Получить статьи с нескольких страниц

введи число:""")

if flag == "1":
    sum = main_page_article(url)
    print(f"Количество статей:{len(sum)}  \nСтатьи сохранены в файл article.txt")
    time.sleep(10)
else:
    sum = multiple_pages_article()
    print(f"Количество статей:{len(sum)}  \nСтатьи сохранены в файл article.txt")
    time.sleep(10)

