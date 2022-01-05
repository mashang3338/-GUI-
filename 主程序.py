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
#导入翻译模块
import fanyi
#导入crawl_novel模块
import crawl_novel
root = Tk()
root.geometry("1000x1000+500+150")
root.resizable(0, 0)
root.title("小说下载")
url_list = []

number = 0




loading = loading.LoadingBar()

#开始按钮，加载loading
def start_load():
    loading.show(speed=2)
    call_back()

#爬取并显示
def call_back():
    content = crawl_novel.get_url_list_and_get_novel(2)
    # text.insert(END, novel_chapter)
    for i in content:
        text.insert(END, i.text)
        text.insert(END,"\r\n")
        text.insert(END,"\r\n")


#结束
def stop_load():
    loading.close()


find_button = Button(root,
                     text="开始执行程序",
                     font=("宋体", 12),
                     command=start_load)
# command=start)
find_button.grid(row=2,column=2)
#下一章按钮
next_button = Button(root,
                     text="下一章",
                     font=("宋体", 12),
                     command=call_back)
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

#翻译按钮
# fanyi_button = Button(root,
#                      text="翻译",
#                      font=("宋体", 12),
#                      command=test.get_content(aim_path=r"D:\base\第一章：醒来（下）.txt"))
# fanyi_button.grid(row=2,column=4)





# main()
mainloop()

