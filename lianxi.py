#FRAME
from tkinter import *

Label(text="天王盖地虎").pack()

separator = Frame(height=2, bd=1, relief=RIDGE)#relief是边框样式
separator.pack(fill=X, padx=5, pady=5)

Label(text="小鸡炖蘑菇").pack()

mainloop()


