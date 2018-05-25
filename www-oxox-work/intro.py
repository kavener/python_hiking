import tkinter

# 实例化一个Tk()类

root = tkinter.Tk()

I_Love = tkinter.Label(root, text="我喜欢tkinter", bg="red", fg='white')
I_Love.pack(fill=tkinter.BOTH, expand=True)

Misson = tkinter.Label(root, text="学习窗口", bg="red", fg='white')
Misson.pack()


root.mainloop()