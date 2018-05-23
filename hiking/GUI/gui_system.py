# 学习基于Tk的GUI编程

from tkinter import *

# top = Tk()
# btn1 = Button()
# btn2 = Button()
# btn1.pack()
# btn2.pack()
#
#
# # 为控件添加行为
# def clicked():
#     print("执行控件行为...")
#
# Label(text="I'm in the first window!").pack()
# # second = Toplevel()
# # Label(second,text="I'm in the second window!").pack()
#
# # 使用config同时控制控件多个属性
# btn1.config(text='btn1:Click me!', command=clicked)
# btn2.config(text='btn2:click me!', command=clicked)
#
# for i in range(10):
#     Button(text=i).pack()

top = Tk()
def callback(event):
    print(event.x, event.y)

top.bind('<Button-1>', callback)
mainloop()