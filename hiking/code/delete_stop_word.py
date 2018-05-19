import re
import variable_id as vbs
import codecs


def stop_word():
    cut_words = open('./../data/cut_result.txt').readlines()
    fh = open("./../data/cut_result_Nostoped.txt", "w")
    for cut_word in cut_words:
        pat = ',|，|。|？|、|\?|、|！|\（|\）|:|；|\.|\+|可能|得|吧|怎样|其他|那|的|了|地|啊|哦|n|\\|\!|着|与|感觉|也|前|非常|挺|确实|起来|就是|啦|其实|一句|由于|做|台|一下|真心|太|呢|还有|么|其它'
        # 停用词表
        new_tmp = []
        for j in cut_word:
            # 去掉无意义的句子
            news = re.sub(pat, "", j)
            new_tmp.append(news)
        for item in new_tmp:
            fh.write(item)
    fh.close()


# stop_word()

def make_pat():
    pat = ',|，|。|？|、|\?|、|！|\（|\）|:|；|\.|\+|可能|得|吧|怎样|其他|那|的|了|地|啊|哦|n|\\|\!|着|与|感觉|也|前|非常|挺|确实|起来|就是|啦|其实|一句|由于|做|台|一下|真心|太|呢|还有|么|其它|'

    with open("./../useful/1896_stop_word.txt", 'r', encoding='utf-8') as file_object:
        data = file_object.readlines()
        for item in data:
            new_tmp_1 = item.replace(' ', '')
            new_tmp_2 = new_tmp_1.replace('\n', '|')
            # print(new_tmp_2)
            pat += new_tmp_2
        print(pat)
        return pat


def stop_word_update():
    pat = ',|，|。|？|-|-|、|\?|、|！|\（|\）|:|；|\.|\+|可能|得|吧|怎样|其他|那|的|了|地|啊|哦|n|\|\!|着|与|感觉|也|前|非常|挺|确实|起来|就是|啦|其实|一句|由于|做|台|一下|真心|太|呢|还有|么|其它|很|非常|就是|确实|更加|更|这次|但是|为|能|吧|把|总之|但|要|只|一次|拿|不过|会|时候|又|说|而且|我|一些|一个|虽然|没有|多|和|不是|都|个|这样|被|跟|知道|应该|以|对|过|时'
    # pat=make_pat()
    # pat = ',|，|。|？|、|\?|、|！|\（|\）|:|；|\.|\+|可能|得|吧|怎样|其他|那|的|了|地|啊|哦|n|\\|\!|着|与|感觉|也|前|非常|挺|确实|起来|就是|啦|其实|一句|由于|做|台|一下|真心|太|呢|还有|么|其它|'
    cut_words = open('./../data/cut_result.txt').readlines()
    fh = open("./../data/cut_result_Nostoped.txt", "w")
    for cut_word in cut_words:
        # 停用词表
        new_tmp = []
        for j in cut_word:
            # 去掉无意义的句子
            news = re.sub(pat, "", j)
            new_tmp.append(news)
        for item in new_tmp:
            fh.write(item)
    fh.close()


# stop_word_update()

def stop_word_id():
    while True:
        if vbs.semaphore == 3:
            print("去停用词...")
            stop_word_update()
            break
    print("去停用词完成.")
    vbs.semaphore = 4


def make_pat():
    pat = ',|，|。|？|、|\?|、|！|\（|/|\）|\\|:|；|\.|\+|可能|得|吧|怎样|其他|那|的|了|地|啊|哦|n|\\|\!|着|与|感觉|也|前|非常|挺|确实|起来|就是|啦|其实|一句|由于|做|台|一下|真心|太|呢|还有|么|其它|'

    with open("./../useful/1896_stop_word.txt", 'r', encoding='utf-8') as file_object:
        data = file_object.readlines()
        for item in data:
            new_tmp_1 = item.replace(' ', '')
            new_tmp_2 = new_tmp_1.replace('\n', '|')
            # print(new_tmp_2)
            pat += new_tmp_2
        print(pat)
        return pat
# make_pat()
