#导入加载进度条类
import loading

import tkinter
import requests
from bs4 import BeautifulSoup
# 下面是TKINTER
from requests import get, post
from fake_useragent import UserAgent
from lxml import etree
from tkinter import *
from tkinter import messagebox
from time import time, sleep
from multiprocessing.dummy import Pool
import threading
from threading import Thread
from tkinter.messagebox import *
import time
from tkinter import ttk
#导入翻译文件
import fanyi
root = Tk()
root.geometry("1000x1000+500+150")
root.resizable(0, 0)
root.title("小说下载")
url_list = []

number = 0


loading = loading.LoadingBar()
# loading.show(speed=4)


def get_url_list():
    #开启滚动条.......#这里的滚动条功能后面参照其他文件写出来
    loading.show()
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
    #关闭滚动条
    loading.close()
    showinfo('提示','小说URL列表获取完成')


def get_novel():
    global number
    number += 1
    url = url_list[number]
    header = {"User-Agent": UserAgent().random}
    html = get(url=url, headers=header)
    data = html
    data.encoding = "utf-8"
    res = data.text
    soup = BeautifulSoup(res, 'lxml')
    #获取章节名
    novel_chapter = soup.find('h1').text
    text.insert(END, novel_chapter)
    print(novel_chapter)
    content = soup.find_all('p')
    for i in content:
        text.insert(END, i.text)
        text.insert(END,"\r\n")
        text.insert(END,"\r\n")
    print(content)


# tkinter.Button(root, text='关闭滚动条', command=loading.close).grid(row=3,column=1)
# tkinter.Button(root, text='开启滚动条', command=loading.show).grid(row=3,column=2)

#开始按钮
find_button = Button(root,
                     text="开始执行程序",
                     font=("宋体", 12),
                     command=get_url_list)
# command=start)
find_button.grid(row=2,column=2)
#下一章按钮
next_button = Button(root,
                     text="下一章",
                     font=("宋体", 12),
                     command=get_novel)
next_button.grid(row=2,column=3)

#label
show_label = Label(root,
                  text="小说章节内容：",
                  font=("宋体", 12),
                  anchor="w")

show_label.grid(row=1,column=1)
#TEXT滚动条
scroll = tkinter.Scrollbar()
# 放到窗口的右侧, 填充Y竖直方向
scroll.grid(row=2,column=1)
#展示小说内容组件
text = Text(root, font=("宋体", 12),yscrollcommand=scroll.set)
text.grid(row=2,column=1)

#
#
# # 两个控件关联
# scroll.config(command=text.yview)
# text.config(yscrollcommand=scroll.set)

#调用翻译函数
test = fanyi.Get_Fanyi()
# test.get_content(aim_path=r"D:\base\第一章：醒来（下）.txt")
#测试
def callback():
    print("这是测试！")
#翻译按钮
fanyi_button = Button(root,
                     text="翻译",
                     font=("宋体", 12),
                     command=test.get_content(aim_path=r"D:\base\第一章：醒来（下）.txt"))
fanyi_button.grid(row=2,column=4)





# main()
mainloop()

