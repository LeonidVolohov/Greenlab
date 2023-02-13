'''Сколько HTML-тегов в коде главной страницы сайта greenatom.ru? Сколько из них содержит атрибуты? 
Напиши скрипт на Python, который выводит ответы на вопросы выше'''

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen


def parse_page(url: str) -> BeautifulSoup:
    header = {"User-Agent": "Mozilla/5.0"}
    request = Request(url, headers=header)
    return BeautifulSoup(urlopen(request), "html.parser")

def count_all_tags(soup: BeautifulSoup) -> int:
    return len(soup.findAll())

def count_all_tags_with_attributes(soup: BeautifulSoup) -> int:
    attr_amount = 0
    for tag in soup.findAll():
        if tag.attrs: attr_amount += 1
    return attr_amount


if __name__ == "__main__":
    greenatom_link = "https://greenatom.ru/"
    soup = parse_page(greenatom_link)

    print("Total amount of tags on page is: " + str(count_all_tags(soup)))
    print("Total amount of tags with attributes on page is: " + str(count_all_tags_with_attributes(soup)))
