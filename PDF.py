
#本文件目标——创建PDF转图片的类——进一步的话可以对PDF进行进一步操作比如合并、提取文字等
import os
from PyPDF2 import PdfFileReader, PdfFileWriter
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from tkinter.ttk import Progressbar
from time import sleep
from threading import Thread
import sys, fitz
import os
import datetime


class Window():
    def __init__(self):#初始化操作——生成窗口、按钮等
        self.root = root = tkinter.Tk()

        self.label = tkinter.Label(root, text='选择目录')#这里的选择目录应当是选择文件
        self.label.grid(row=3, column=0)
        self.entryDir = tkinter.Entry(root)
        self.entryDir.grid(row=3, column=1)
        self.BrowserDirButton = tkinter.Button(root, text='浏览', command=self.BrowserDir)#注意这里的回调函数browserdir,指打开文件管理器
        self.BrowserDirButton.grid(row=3, column=2)

        self.ButtonCov = tkinter.Button(root, text='开始处理', command=self.Conv, )#这里的回调函数是主要的转换功能
        self.ButtonCov.grid(row=4, column=0)

    def BrowserDir(self):
        directory = tkinter.filedialog.asksaveasfilename(title='Python')#值即选择文件路径
        if directory:#输出框内容
            self.entryDir.delete(0, tkinter.END)
            self.entryDir.insert(tkinter.END, directory)

    def Split(self):
        #获取输入框内容
        path = self.entryDir.get()
        #进度条，嵌套在上个函数里
        def _prog():
            top = tkinter.Toplevel(self.root)
            # top.attributes("-", 1)
            top.attributes("-topmost", 1)
            top.title("进度条")
            tkinter.Label(top, text="正在处理PDF，请稍候…").pack()
            prog = Progressbar(top, mode="indeterminate")#直接实例化ttk的方法

            prog.pack()
            prog.start()#进度条开始
            #转换

            pdf = PdfFileReader(path)
            for page in range(pdf.getNumPages()):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf.getPage(page))
                output = f'D:/base/temp/NO{page}.pdf'
                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
            sleep(0.5)
            prog.stop()#进度条结束
            top.destroy()
            tkinter.messagebox.showinfo("提示：", "已完成！")

        t = Thread(target=_prog)#线程,实例化_prog方法
        t.start()#执行——prog方法

    def Conv(self):
        #获取输入框内容
        path = self.entryDir.get()
        #进度条，嵌套在上个函数里
        def _prog():
            top = tkinter.Toplevel(self.root)
            # top.attributes("-", 1)
            top.attributes("-topmost", 1)
            top.title("进度条")
            tkinter.Label(top, text="正在处理PDF，请稍候…").pack()
            prog = Progressbar(top, mode="indeterminate")#直接实例化ttk的方法
            prog.pack()
            prog.start()#进度条开始

            #转换
            pdfDoc = fitz.open(path)
            for pg in range(pdfDoc.pageCount):
                page = pdfDoc[pg]
                rotate = int(0)
                # 每个尺寸的缩放系数为1.3，这将为我们生成分辨率提高2.6的图像。
                # 此处若是不做设置，默认图片大小为：792X612, dpi=72
                zoom_x = 1.33333333  # (1.33333333-->1056x816)   (2-->1584x1224)
                zoom_y = 1.33333333
                mat = fitz.Matrix(zoom_x, zoom_y).preRotate(rotate)
                pix = page.getPixmap(matrix=mat, alpha=False)

                # if not os.path.exists(imagePath):
                #     os.makedirs(imagePath)  # 可以以后新增用户选择文件存储目录按钮

                pix.writePNG(path + '/' + 'images_%s.png' % pg)  # 将图片写入指定的文件夹内
            for page in range(pdfDoc.getNumPages()):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdfDoc.getPage(page))
                output = f'D:/base/temp/picNO{page}.pdf'
                with open(output, 'wb') as output_pdf:
                    pdf_writer.write(output_pdf)
            sleep(0.5)
            prog.stop()#进度条结束
            top.destroy()
            tkinter.messagebox.showinfo("提示：", "已完成！")

        t = Thread(target=_prog)#线程,实例化_prog方法
        t.start()#执行——prog方法

    def mainloop(self):
        self.root.minsize(330, 190)
        self.root.maxsize(330, 170)
        self.root.title('PDF处理器')
        self.root.mainloop()


if __name__ == "__main__":
    window = Window()
    window.mainloop()
