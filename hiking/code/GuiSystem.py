from tkinter import *

root = Tk()

root.title("基于电商评论的用户情感分析的系统")

# 窗口大小
width = 600
height = 500
# 窗口居中显示
root.geometry(
    '%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
# 窗口最大值
root.maxsize(width, height)
# 窗口最小值
root.maxsize(width, height)

root.mainloop()
