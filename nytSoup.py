import requests
from bs4 import BeautifulSoup


def wired_scrape():
    wired = requests.get("https://www.wired.com/category/security/")
    # wired = wired.
    wiredSoup = BeautifulSoup(wired.text, "html.parser")

    # title = wiredSoup.title.text
    news = wiredSoup.find_all("li", class_="card-component__description")
    for x in news:
        heading = x.h2.text
        link = "https://www.wired.com" + x.a.get("href")
        paragraph = pWired(link)
        print(heading)
        print(paragraph)


def pWired(link):
    paraHtml = requests.get(link).text
    paraSoup = BeautifulSoup(paraHtml, "html.parser")

    paras = paraSoup.find_all("p")
    para_div = paraSoup.find("div", class_="article__body").p
    for x in paras:
        a = x.text
        print()
    print()
    return paras[:2]


wired_scrape()

