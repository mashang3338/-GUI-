
#这个先封装成类，完善爬取小说的功能，想不到其他的就先实现用户输入章节数，爬取指定数量的章节内容
from requests import get, post
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def __init__(self):
    print("开始进行爬取小说!")

def get_url_list_and_get_novel(number):
    number = number
    # global number
    url_list = []
    #获取20章
    time = 20
    novel_url = "http://www.31xs.org/5/5430/3496470.html"
    while time > 0:
        header = {"User-Agent": UserAgent().random}
        html = get(url=novel_url, headers=header)
        data = html
        data.encoding = "utf-8"
        res = data.text
        soup = BeautifulSoup(res, 'lxml')
        print(soup.find(class_="bottem2").contents)
        next_url = "http://www.31xs.org" + soup.find(class_="bottem2").contents[7].get('href')
        novel_url = next_url
        print(next_url)
        url_list.append(next_url)
        time -= 1
    print(url_list)
    get_novel(url_list,number)


def get_novel(url_list,number):

    # number += 1
    url = url_list[number]
    header = {"User-Agent": UserAgent().random}
    html = get(url=url, headers=header)
    data = html
    data.encoding = "utf-8"
    res = data.text
    soup = BeautifulSoup(res, 'lxml')
    #获取章节名
    novel_chapter = soup.find('h1').text
    # text.insert(END, novel_chapter)
    print(novel_chapter)
    content = soup.find_all('p')
    return content
    # for i in content:
    #     text.insert(END, i.text)
    #     text.insert(END,"\r\n")
    #     text.insert(END,"\r\n")
    # print(content)