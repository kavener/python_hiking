from wordcloud import WordCloud
import variable_id as vbs
def creat_worldCloud():
    print("创建词云中...")
    f = open('./../data/cut_result_Nostoped.txt','r',encoding="gbk").read()
    wordcloud = WordCloud(background_color="white",font_path='C:\Windows\Fonts\msyh.ttc',width=1920, height=1080, margin=2).generate(f)
    #wordcloud = WordCloud(background_color="grey", max_words=2000,font_path='C:\Windows\Fonts\STZHONGS.TTF',max_font_size=40, random_state=42).generate(f)

    # width,height,margin可以设置图片属性

    # generate 可以对全部文本进行自动分词,但是他对中文支持不好,对中文的分词处理请看我的下一篇文章
    #wordcloud = WordCloud(font_path = r'D:\Fonts\simkai.ttf').generate(f)
    # 你可以通过font_path参数来设置字体集

    #background_color参数为设置背景颜色,默认颜色为黑色

    import matplotlib.pyplot as plt
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

    wordcloud.to_file('./../data/test.png')
    # 保存图片,但是在第三模块的例子中 图片大小将会按照 mask 保存
    print("词云创建完成.")

#creat_worldCloud()

def creat_worldCloud_id():
    while True:
        if vbs.semaphore==4:
            print("分词中...")
            creat_worldCloud()
            break
    print("分词完成.")
    vbs.semaphore=5