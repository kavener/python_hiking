'''
分词
'''
import jieba
import variable_id as vbs
import re
from jieba import posseg


# 分词
# 添加自己的词典
def participle():
    jieba.load_userdict('./../useful/myDict.txt')
    # jieba.load_userdict('E:/Learnsoft/Anaconda3/Lib/site-packages/jieba/dict_self.txt')

    cut_words = open('./../data/pretreatmented_comments.txt').readlines()
    fh = open("./../data/cut_result.txt", "w")
    #

    for i in cut_words:
        i_gb2312 = i.encode('gb2312', 'ignore')
        # i=i.decode('gb2312','ignore').encode('utf-8','ignore')
        # i=i.decode('utf-8')
        # i.decode('utf-8')
        gb2312_utf8 = i_gb2312.decode('gb2312').encode('utf-8')
        # 完美解决编码转换问题
        utf8_unicode = gb2312_utf8.decode('utf-8')
        cut_word = jieba.cut(gb2312_utf8)
        pat = ''
        new_tmp = []
        for j in cut_word:
            # 去掉无意义的句子
            news = re.sub(pat, "", j)
            new_tmp.append(news)
            # print(news)
            # fh.write(news)
        for item in new_tmp:
            fh.write(item + " ")
    fh.close()


# 词频统计：
from jieba import analyse


def word_frequency():
    data = open("./../data/cut_result.txt").read()
    tag = analyse.extract_tags(data, 20)  # 10 个关键词数量
    for items in tag:
        print(items)


# participle()

def participle_id():
    while True:
        if vbs.semaphore == 2:
            print("分词中...")
            participle()
            break
    print("分词完成.")
    vbs.semaphore = 3
