import requests
from bs4 import BeautifulSoup

nyt = requests.get("https://www.nytimes.com/").text
nytNews = BeautifulSoup(nyt, "html.parser")
print(nytNews.title.text)
