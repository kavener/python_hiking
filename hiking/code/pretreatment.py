import jieba
import variable_id as vbs
import re

'''
    文本预处理
    1.删除无意义词
    2.检测句内重复并压缩，机械压缩取词？？？
    3.去掉短句
    5.保存数据
'''


def pretreatment():
    data_comments = open("./../data/jd_thread_comments.txt").readlines()
    # data_comments = open("./../data/meidi_comments.txt").readlines()
    # 加上list和sort使列表保持原来顺序
    tmp = list(set(data_comments))
    tmp.sort(key=data_comments.index)
    fh = open("./../data/pretreatmented_comments.txt", "w")
    # fh_pat=open("./../useful/structure_filter_words.txt").read()
    pat = '&hellip;|&ldquo;|&rdquo;|&deg;|&times;|&mdash;|&quot;|&there4;|&omega;|&yen;|&bull;'
    # pat='！|，|。|？|～|（|）|http://.*?none|!|!|\.|`|\?|@|#|%|^|&|\*|(\|)|\,| |的|    |   | |最后|什么|几个|我|了|们'
    new_tmp = []
    for j in tmp:
        # 去掉无意义的句子
        news = re.sub(pat, "", j)
        new_tmp.append(news)
        # print(news)
        # fh.write(news)

    # 怎么完成压缩去词？  一般为一至四个词语的重复，这样想，怎么完成单个字的去重
    # 其实就是在一句话里面完成，用for检测？

    def delete_repeat(tmp):
        handle = []
        times = 1
        '''
        test1 = "啊啊啊啊啊啊"
        #test1 = "我喜欢我喜欢我喜欢我喜欢我喜欢"
        #test1 = "哈哈哈哈哈哈哈哈"
        test1 = "好差差差差差差差差差差差差差差差差差差差差差啊"
        print("精准模式------------------------")
        re=jieba.cut(test1,cut_all=False)
        for i in re:
            print(i)
    
        print("全模式--------------------------")
    
        '''
        # 全模式分词并且写入lists,然后使用set()，暴力去重
        for words in tmp:
            # 精准模式
            lists = []
            re = jieba.cut(words, cut_all=False)
            for i in re:
                # print(i)
                lists.append(i)

            print("第" + str(times) + "评论分词成功并写入lists列表...")
            # print(lists)
            # print(lists.count('不好'))
            times += 1
            tmp = list(set(lists))
            tmp.sort(key=lists.index)
            # print(tmp)
            for tmp_item in tmp:
                # print("判断重复...")
                if lists.count(tmp_item) > 6:
                    print("出现重复：-----------------------------------------\n\n")
                    print("原句：" + str(lists))

                    print("去词后：" + str(tmp))
                    words = tmp

            handle.append(words)
        return handle

    handle_tmp = delete_repeat(new_tmp)
    print(handle_tmp, len(handle_tmp))

    # 去掉短句
    def delete_short(handle_tmp):
        #
        handled_tmp = []
        for words in handle_tmp:
            if len(words) <= 6:
                print(words)
                continue
            handled_tmp.append(words)
        return handled_tmp

    handled_tmp = delete_short(handle_tmp)
    print(handled_tmp)
    print(len(handle_tmp))
    print(len(handled_tmp))

    # 写入文件
    i = 1
    for item_outside in handled_tmp:
        for item_inside in item_outside:
            fh.write(item_inside)
        print("成功写入第" + str(i) + "句评论")
        i += 1
    fh.close()


# pretreatment()

def pretreatment_id():
    while True:
        # if vbs.semaphore == 0:
        if vbs.semaphore == 1:
            print("数据预处理...")
            pretreatment()
            break
    print("数据预处理完成.")
    vbs.semaphore = 2


def delete_repeat(tmp):
    handle = []
    times = 1
    # 全模式分词并且写入lists,然后使用set()去重
    for words in tmp:
        # 精准模式
        lists = []
        re = jieba.cut(words, cut_all=False)
        for i in re:
            lists.append(i)
        print("第" + str(times) + "评论分词成功并写入lists列表...")
        times += 1
        tmp = list(set(lists))
        tmp.sort(key=lists.index)
        for tmp_item in tmp:
            # 判断重复
            if lists.count(tmp_item) > 6:
                print("出现重复：-----------------------------------------\n\n")
                print("原句：" + str(lists))
                print("去词后：" + str(tmp))
                words = tmp
        handle.append(words)
    return handle
