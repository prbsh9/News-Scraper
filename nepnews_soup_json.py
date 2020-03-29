from bs4 import BeautifulSoup
import requests
import csv


def onlineKhabarNews(x=15):
    '''Gives fresh onlineKhabarNews from internet while parameter x is in which
    you get to chose how many small headlines you want. It will get you a main
    main headline with summery, link to news and other headlines with link'''

    oKhabar = requests.get('https://www.onlinekhabar.com/').text
    onlineKhabarSoup = BeautifulSoup(oKhabar, 'lxml')  # lxml is parser

    # # Main news part
    print('Here is the main news of onlinekhabar')
    print()

    # mainNews = onlineKhabarSoup.find('div', class_='ok__bises--2')
    # print(mainNews.a.text)
    # print()
    # print(mainNews.p.text)
    # print(mainNews.a.get('href'))
    # print()
    # print()
    # print()
    # print()
    # csv_writer.writerow(['onlinekhabar', mainNews.a.text, mainNews.p.text, mainNews.a.get('href')])
    # print('Here is the other news of onlinekhabar')
    print()
    print()
    n = 0
    for oH in onlineKhabarSoup.find_all('h2', class_='post__title'):
        print(oH.text)  # oH stands for other headlines
        print(oH.a.get('href'))
        print()
        csv_writer.writerow(['onlinekhabar', oH.text, None, oH.a.get('href')])
        n += 1
        if n > x:  # x is parameter
            break  # you get to chose how many small headlines you want


def ekantipurKhabarNews():
    '''Gives fresh and realtime ekantipur from internet
    using BeautifulSoup  '''
    e_kantipur = requests.get('https://www.ekantipur.com/').text
    ekantipurSoup = BeautifulSoup(e_kantipur, 'lxml')
    # Main news part
    print('Here is the main headlines of ekantipur')
    print()

    for mainN in ekantipurSoup.find_all('h1'):
        if mainN.a is not None:
            print(mainN.a.text)
            print(mainN.a.get('href'))
            csv_writer.writerow(['ekantipur', mainN.a.text, None, mainN.a.get('href')])
            print()
            print()
    print()
    print()
    print()
    print('Here are the other headlines of ekantipur')
    print()

    extraNews = ekantipurSoup.find('div', class_='more-main-news').find_all('article')
    for otherN in extraNews:
        print(otherN.h2.text)
        print()
        print(otherN.p.text)
        print(otherN.h2.a.get('href'))
        csv_writer.writerow(['ekantipur', otherN.a.text, otherN.p.text, otherN.a.get('href')])
        print()
        print()


if __name__ == '__main__':
    csv_file = open('nepnews.csv', 'w', encoding='utf8', errors='ignore')
    csv_writer = csv.writer(csv_file)
    # csv_writer.writerow(['source', 'headline', 'summary', 'newsLink'])
    onlineKhabarNews()
    ekantipurKhabarNews()
    csv_file.close()
