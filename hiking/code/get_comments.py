#import main
import threading
import time
import use_proxy
import re
import variable_id as vbs
#引入锁机制！！
from threading import Lock
lock = Lock()
#暂时用全局变量用作信号量
semaphore=0

#product_id=1138288
#product_id=5054737

#全局变量i，为页数

#添加一个IP池
all_comments=[]
#打开待写入文件
fh=open("./../data/jd_thread_comments.txt","w")

#暂时用全局变量来代替信号量
thread_num=1
i=0
k=0
this_page=1
in_this_page=0
comments_num=0
def threadfun():  # 线程任务函数 threadfun()
    global comments_num
    global this_page
    global thread_num
    global i
    global k
    global in_this_page

    while i < 4:
        #多线程通信问题导致重复爬取16次
        in_this_page+=1
        url ="https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv82248&productId="+str(vbs.product_id)+"&score="+ str(i) +"&sortType=5&page=" + str(this_page) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
        print("正在爬取第" + str(in_this_page) + "页评论...")
        data=use_proxy.use_proxy(use_proxy.proxy_addr,url)
        #正则关键是找到开头的匹配独立字符
        patComments = '"topped".*?"content":"(.*?)","creationTime.*?referenceImage"'
        results = re.compile(patComments).findall(str(data))
        for j in results:
            fh.write(str(j)+"\n")
            comments_num+=1
        print("第"+str(in_this_page)+"页写入完成...")
        this_page+=1
        lock.acquire()
        if(this_page>100):
            if(i==1):
                print("￣へ￣--------全部推荐差评信息爬取完成--------￣へ￣")
            elif(i==2):
                print("╮(╯﹏╰）╭--------全部推荐中评信息爬取完成--------╮(╯﹏╰）╭")
            elif(i==3):
                print("ヾ(◍°∇°◍)ﾉﾞ--------全部推荐好评信息爬取完成--------ヾ(◍°∇°◍)ﾉﾞ")
            elif(i==0):
                print("(^_−)☆--------全部初现推荐信息爬取完成--------(^_−)☆")
            i += 1
            this_page=0
        lock.release()

    while k < 4:
        # 多线程通信问题导致重复爬取16次
        in_this_page += 1
        url = "https://club.jd.com/comment/skuProductPageComments.action?callback=fetchJSON_comment98vv82248&productId=" + str(
            vbs.product_id) + "&score=" + str(i) + "&sortType=6&page=" + str(
            this_page) + "&pageSize=10&isShadowSku=0&rid=0&fold=1"
        print("正在爬取第" + str(in_this_page) + "页评论...")
        data = use_proxy.use_proxy(use_proxy.proxy_addr, url)
        # 正则关键是找到开头的匹配独立字符
        patComments = '"topped".*?"content":"(.*?)","creationTime.*?referenceImage"'
        results = re.compile(patComments).findall(str(data))
        for j in results:
            fh.write(str(j) + "\n")
            comments_num += 1
        print("第" + str(in_this_page) + "页写入完成...")
        this_page += 1
        lock.acquire()
        if (this_page > 100):
            if (k == 1):
                print("￣へ￣--------全部推荐差评信息爬取完成--------￣へ￣")
            elif (k == 2):
                print("╮(╯﹏╰）╭--------全部推荐中评信息爬取完成--------╮(╯﹏╰）╭")
            elif (k == 3):
                print("ヾ(◍°∇°◍)ﾉﾞ--------全部推荐好评信息爬取完成--------ヾ(◍°∇°◍)ﾉﾞ")
            elif (k == 0):
                print("(^_−)☆--------全部初现推荐信息爬取完成--------(^_−)☆")
            k += 1
            this_page = 0
        lock.release()

    print("第" + str(thread_num) + "个线程成功退出！")
    thread_num += 1
    #data=jd_comments.use_proxy(proxy_addr,url)
    #patComments = '"content":"(.*?)","creationTime"|"content":"(.*?)<div class=\'uploadimgdiv\'>'
    #results = re.compile(patComments).findall(str(data))
    # print(data)
    #all_comments.append(results)
#做一个全局的url池，并且实时写入数据

def others():
    while True:
        if thread_num>16:
            fh.close()
            vbs.semaphore=1
            #print(vbs.semaphore)
            print("爬取数据完成...")
            break



#大力出奇迹233
ta = threading.Thread(target=threadfun)  # 创建一个线程ta，执行 threadfun()
tb = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tc = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
td = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
te = threading.Thread(target=threadfun)  # 创建一个线程ta，执行 threadfun()
tf = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tg = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
th = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
ti = threading.Thread(target=threadfun)  # 创建一个线程ta，执行 threadfun()
tj = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tk = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tl = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tm = threading.Thread(target=threadfun)  # 创建一个线程ta，执行 threadfun()
tn = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
to = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
tp = threading.Thread(target=threadfun)  # 创建一个线程tb，执行threadfun()
others = threading.Thread(target=others)  # 创建一个线程tb，执行threadfun()

def get_comments():
    ta.start()  # 调用start()，运行线程
    tb.start()  # 调用start()，运行线程
    tc.start()  # 调用start()，运行线程
    td.start()  # 调用start()，运行线程
    te.start()  # 调用start()，运行线程
    tf.start()  # 调用start()，运行线程
    tg.start()  # 调用start()，运行线程
    th.start()  # 调用start()，运行线程
    tj.start()  # 调用start()，运行线程
    tk.start()  # 调用start()，运行线程
    tl.start()  # 调用start()，运行线程
    tm.start()  # 调用start()，运行线程
    tn.start()  # 调用start()，运行线程
    to.start()  # 调用start()，运行线程
    tp.start()  # 调用start()，运行线程
    ti.start()  # 调用start()，运行线程
    others.start()

#get_comments()

