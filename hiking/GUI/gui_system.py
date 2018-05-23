# from tkinter import *
#
#
# class TYST(Tk):
#     def __init__(self):
#         Tk.__init__(self)
#         self.scrollbar = Scrollbar(self)
#         self.scrollbar.pack(side=RIGHT, fill=Y)
#
#         self.mylist = Listbox(self, yscrollcommand=self.scrollbar.set)
#
#         for line in range(100):
#             # self.mylist.insert(END,str(line))
#             self.mylist.insert(END, "This is line number " + str(line))
#         self.mylist.pack(side=LEFT, fill=BOTH)
#
#         self.scrollbar.config(command=self.mylist.yview)
#
#
# def main():
#     tyst = TYST()
#     for i in range(100):
#         tyst.after(100, tyst.mylist.yview_moveto(i / 100), tyst.update())  # 滚动的同时要不停刷新
#
#     tyst.mainloop()
#
#
# if __name__ == '__main__':
#     main()

from tkinter import *

root = Tk()
text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background = "yellow", foreground = "blue")
text.tag_config("start", background = "black", foreground = "green")
root.mainloop()