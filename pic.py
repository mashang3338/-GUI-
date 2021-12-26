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
    def __init__(self):
        self.root = root = tkinter.Tk()

        self.label = tkinter.Label(root, text='选择目录')
        self.label.grid(row=3, column=0)
        self.entryDir = tkinter.Entry(root)
        self.entryDir.grid(row=3, column=1)
        self.BrowserDirButton = tkinter.Button(root, text='浏览', command=self.BrowserDir)
        self.BrowserDirButton.grid(row=3, column=2)

        self.ButtonCov = tkinter.Button(root, text='开始处理', command=self.Conv, )
        self.ButtonCov.grid(row=4, column=0)

    def BrowserDir(self):
        directory = tkinter.filedialog.askdirectory(title='Python')
        if directory:
            self.entryDir.delete(0, tkinter.END)
            self.entryDir.insert(tkinter.END, directory)

    def Conv(self):
        path = self.entryDir.get()

        def _prog():
            top = tkinter.Toplevel(self.root)
            top.attributes("-toolwindow", 1)
            top.attributes("-topmost", 1)
            top.title("进度条")
            tkinter.Label(top, text="正在处理图片，请稍候…").pack()
            prog = Progressbar(top, mode="indeterminate")
            prog.pack()
            prog.start()

            for file in os.listdir(path):
                if file[-4:] in ('.bmp', '.jpg', 'jpeg', '.gif', '.png', '.BMP', '.JPG', 'JPGE', '.GIF', '.PNG'):
                    f_img = path + "/" + file
                    image = Image.open(f_img)
                    newwidth = int(image.size[0] / 2)
                    newheight = int(image.size[1] / 2)
                    image = image.resize((newwidth, newheight), PIL.Image.NEAREST)
                    image.save(f_img)
                    sleep(0.5)
            prog.stop()
            top.destroy()
            tkinter.messagebox.showinfo("提示：", "已完成！")

        t = Thread(target=_prog)
        t.start()

    def mainloop(self):
        self.root.minsize(330, 190)
        self.root.maxsize(330, 170)
        self.root.title('图片批量处理器')
        self.root.mainloop()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
