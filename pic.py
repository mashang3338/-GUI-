本文件目标——创建PDF转图片的类——进一步的话可以对PDF进行进一步操作比如合并、提取文字等
import os
from PIL import Image, ImageEnhance
import PIL
import tkinter
import tkinter.filedialog
import tkinter.messagebox

from tkinter.ttk import Progressbar
from time import sleep
from threading import Thread


class Window():
    def __init__(self):#初始化操作——生成窗口、按钮等
        self.root = root = tkinter.Tk()

        self.label = tkinter.Label(root, text='选择目录')
        self.label.grid(row=3, column=0)
        self.entryDir = tkinter.Entry(root)
        self.entryDir.grid(row=3, column=1)
        self.BrowserDirButton = tkinter.Button(root, text='浏览', command=self.BrowserDir)#注意这里的回调函数browserdir,指打开文件管理器
        self.BrowserDirButton.grid(row=3, column=2)

        self.ButtonCov = tkinter.Button(root, text='开始处理', command=self.Conv, )#这里的回调函数是主要的转换功能
        self.ButtonCov.grid(row=4, column=0)

    def BrowserDir(self):
        directory = tkinter.filedialog.askdirectory(title='Python')#值即选择目录路径
        if directory:#输出框内容
            self.entryDir.delete(0, tkinter.END)
            self.entryDir.insert(tkinter.END, directory)

    def Conv(self):
        #获取输入框内容
        path = self.entryDir.get()
        #进度条，嵌套在上个函数里
        def _prog():
            top = tkinter.Toplevel(self.root)
            top.attributes("-fullscreen", 1)
            top.attributes("-topmost", 1)
            top.title("进度条")
            tkinter.Label(top, text="正在处理图片，请稍候…").pack()
            prog = Progressbar(top, mode="indeterminate")#直接实例化ttk的方法

            prog.pack()
            prog.start()#进度条开始
            #转换
            for file in os.listdir(path):
                if file[-4:] in ('.bmp', '.jpg', 'jpeg', '.gif', '.png', '.BMP', '.JPG', 'JPGE', '.GIF', '.PNG'):
                    f_img = path + "/" + file#新图片保存路径
                    image = Image.open(f_img)
                    newwidth = int(image.size[0] / 2)
                    newheight = int(image.size[1] / 2)
                    image = image.resize((newwidth, newheight), PIL.Image.NEAREST)#图片改为一半大小
                    image.save(f_img)
                    sleep(0.5)
            prog.stop()#进度条结束
            top.destroy()
            tkinter.messagebox.showinfo("提示：", "已完成！")

        t = Thread(target=_prog)#线程,实例化_prog方法
        t.start()#执行——prog方法

    def mainloop(self):
        self.root.minsize(330, 190)
        self.root.maxsize(330, 170)
        self.root.title('图片批量处理器')
        self.root.mainloop()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
