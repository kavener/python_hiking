from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import *
from gensim.models import Word2Vec
import variable_id
import get_comments as gc
import pretreatment as ptt
import participle as ple
import delete_stop_word as dsw
import build_word2vec as bd2
import create_wordCloud as cwd
import kmeans as ks
def frame(master):
    """将共同的属性作为默认值, 以简化Frame创建过程"""
    w = Frame(master)
    w.pack(side=TOP, expand=YES, fill=BOTH)
    return w

def button(master, text, command):
    """提取共同的属性作为默认值, 使Button创建过程简化"""
    w = Button(master, text=text, command=command, width=6)
    w.pack(side=LEFT, expand=YES, fill=BOTH, padx=2, pady=2)
    return w

def play_result(filename):
    with open(filename) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())

def get_id_comments():
    fh = open("./variable_id.py", "w")
    fh.write("product_id=" + filename.get())
    fh.close()
    # 清除原评论信息
    with open("./../data/jd_thread_comments.txt",'w') as file:
        file.write('')
    # 爬取评论信息
    gc.get_comments()

def pretreatment():
    ptt.pretreatment()
def input_id_gets():
    print("f")

root = Tk()

root.title("基于电商评论的用户情感分析的系统")

main_menu = Menu()  # 创建最上层主菜单
# 创建Calculator菜单, 并加入到主菜单
calc_menu = Menu(main_menu, tearoff=0)
calc_menu.add_command(label='Quit', command=lambda: exit())
main_menu.add_cascade(label='File', menu=calc_menu)

# 创建View菜单, 并加入到主菜单
# 其中"Show Thousands Separator"菜单项是一个Checkbutton
text = StringVar()
sep_flag = IntVar()
sep_flag.set(0)
view_menu = Menu(main_menu, tearoff=0)
view_menu.add_checkbutton(label='About', variable=sep_flag,
                          command=lambda t=text: t.set(add_sep(t.get())))
main_menu.add_cascade(label='View', menu=view_menu)

root['menu'] = main_menu  # 将主菜单与root绑定


# 窗口大小
width = 600
height = 500
# 窗口居中显示
root.geometry('%dx%d+%d+%d' % (width, height, (root.winfo_screenwidth() - width) / 2, (root.winfo_screenheight() - height) / 2))
# 窗口最大值
# top.maxsize(width, height)
# 窗口最小值
root.minsize(width, height)

def load():
    with open(filename.get()) as file:
        contents.delete('1.0', END)
        contents.insert(INSERT, file.read())
def save():
    with open(filename.get(), 'w') as file:
        file.write(contents.get('1.0', END))

frm_input = Frame(root)
Label(frm_input, text="请输入产品ID").pack(side=LEFT)
filename = Entry(frm_input)
filename.pack(side=LEFT, expand=True, fill=X)
Button(frm_input, text='爬取', command=get_id_comments).pack(side=LEFT)
frm_input.pack(side=TOP)

frm_function = Frame(root)
Button(frm_function, text='预处理', command=pretreatment).pack(side=LEFT)
Button(frm_function, text='分词', command=input_id_gets).pack(side=LEFT)
Button(frm_function, text='构建词云', command=input_id_gets).pack(side=LEFT)
Button(frm_function, text='训练词向量', command=input_id_gets).pack(side=LEFT)
Button(frm_function, text='K-means聚类', command=input_id_gets).pack(side=LEFT)
frm_function.pack(side=TOP)

frm_edit = Frame(root)

frm_edit_top = Frame(frm_edit)
contents = ScrolledText(frm_edit_top)
contents.pack(side=BOTTOM, expand=True, fill=BOTH)
frm_edit_top.pack(side=TOP)

frm_edit_bottom = Frame(frm_edit)
Button(frm_edit_bottom, text='Save', command=save).pack(side=BOTTOM)
frm_edit_bottom.pack(side=BOTTOM)

frm_edit.pack(side=TOP)

mainloop()