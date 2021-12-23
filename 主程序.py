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

root = Tk()
root.geometry("800x600+500+150")
root.resizable(0, 0)
root.title("小说下载")
url_list = []

number = 0

#下面是加载滚动条效果
def formatForm(form, width, heigth):
    """设置居中显示"""
    # 得到屏幕宽度
    win_width = form.winfo_screenwidth()
    # 得到屏幕高度
    win_higth = form.winfo_screenheight()
    # 计算偏移量
    width_adjust = (win_width - width) / 2
    higth_adjust = (win_higth - heigth) / 2
    form.geometry("%dx%d+%d+%d" % (width, heigth, width_adjust, higth_adjust))

#加载组件类
class LoadingBar(object):
#窗体大小
    def __init__(self, width=200):
        # 存储显示窗体
        self.__dialog = None
        # 记录显示标识
        self.__showFlag = True
        # 设置滚动条的宽度
        self.__width = width
        # 设置窗体高度
        self.__heigth = 20

    def show(self, speed=10, sleep=0):
        """显示的时候支持重置滚动条速度和标识判断等待时长"""
        # 防止重复创建多个
        if self.__dialog is not None:
            return
        # 线程内读取标记的等待时长（单位秒）
        self.__sleep = sleep

        # 创建窗体
        self.__dialog = tkinter.Toplevel()
        # 去除边框
        self.__dialog.overrideredirect(-1)
        # 设置置顶
        self.__dialog.wm_attributes("-topmost", True)
        formatForm(self.__dialog, self.__width, self.__heigth)
        # 实际的滚动条控件
        self.bar = ttk.Progressbar(self.__dialog, length=self.__width, mode="indeterminate",
                                   orient=tkinter.HORIZONTAL)
        self.bar.pack(expand=True)
        # 数值越小，滚动越快
        self.bar.start(speed)
        # 开启新线程保持滚动条显示
        t = threading.Thread(target=self.waitClose)
        t.setDaemon(True)
        t.start()

    def waitClose(self):
        # 控制在线程内等待回调销毁窗体
        while self.__showFlag:
            time.sleep(self.__sleep)

        # 非空情况下销毁
        if self.__dialog is not None:
            self.__dialog.destroy()

        # 重置必要参数
        self.__dialog = None
        self.__showFlag = True

    def close(self):
        # 设置显示标识为不显示
        self.__showFlag = False

#loading就是上面定义的类
loading = LoadingBar()
# loading.show(speed=5)

def start():

    get_url_list()
    loading.close()

#
# def close_loading():
#     loading.close()

def get_url_list():
    # #开启滚动条
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
                     # command=get_url_list)
command=start)
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



# 两个控件关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


# main()
mainloop()