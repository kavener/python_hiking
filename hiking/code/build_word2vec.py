import variable_id as vbs
from gensim.models import word2vec
from gensim.models import Word2Vec
from sklearn.cluster import KMeans
import rlcompleter


def comments_to_comment():
    sentences = []
    data = open("./../data/cut_result_Nostoped.txt").readlines()
    for str in data:
        # print(i)
        sentence = []
        y = ''
        tmp = 0
        for x in str:
            if (tmp == 0):
                tmp += 1
                continue
            if (x != "\n" and x != " "):
                y += x

            elif (x == " "):
                sentence.append(y)
                y = ''
                continue

        # print("不断构建内层...")
        sentences.append(sentence)
        # print("成功构建一个外层")
    print("txt to sentences success.")
    return sentences


def build_word2vec():
    classCount = 10
    sentences = comments_to_comment()
    model = word2vec.Word2Vec(sentences, size=200)
    model.save("./../data/comments.model")
    keys = model.wv.vocab.keys()
    wordvector = []
    for key in keys:
        wordvector.append(model[key])
    print(keys)


'''

def model_test():
    model = Word2Vec.load("./../data/comments.model")
    print(model)
    try:
        y1 = model.similarity(u"清晰","电视")
    except KeyError:
        y1 = 0
    print ("【苹果】和【好用】的相似度为：",y1)
    ss='好'
    y3 = model.most_similar(ss, topn=20)
    print("和【"+ss+"】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")
    ss = '不好'
    y3 = model.most_similar(ss, topn=20)
    print("和【" + ss + "】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")



'''
'''
def wordsCluster():
    
    #textUrl:输入文本的本地路径，
    #fencijieguo：分词结果存储到本地路径，
    #vectorSize：词向量大小，
    #classCount：分类大小


    
    classCount = 10
    # word2vec向量化
    #model = Word2Vec(LineSentence(fencijieguo), size=vectorSize, window=5, min_count=3, workers=4)
    model = Word2Vec.load("./../data/comments.model")
    # 获取model里面的说有关键词
    keys = model.wv.vocab.keys()

    # 获取词对于的词向量
    wordvector = []
    for key in keys:
        wordvector.append(model[key])

    # 分类
    clf = KMeans(n_clusters=classCount)
    s = clf.fit(wordvector)
    print(s)

    # 获取到所有词向量所属类别
    labels = clf.labels_

    # 把是一类的放入到一个集合
    classCollects = {}
    for i in range(len(keys)):
        if labels[i] in classCollects.keys():
            classCollects[labels[i]].append(keys[i])
            print("eeeeeeee")
        else:
            #classCollects[labels[i]] = [keys[i]]
            #classCollects[labels[i]] = keys[i]
            print("mmmmmm")

    return classCollects
    
    '''


# build_word2vec()
# model_test()


def build_word2vec_id():
    while True:
        if vbs.semaphore == 5:
            print("建立gensim.word2vec模型...")
            build_word2vec()
            break
    print("gensim.word2vec模型建立完成.")
    vbs.semaphore = 6


def model_test():
    comments_to_comment()
    build_word2vec()
    model = Word2Vec.load("./../data/comments.model")
    print(model)
    try:
        y1 = model.similarity(u"好", "不好")
    except KeyError:
        y1 = 0
    print("【好】和【不好】的相似度为：", y1)

    y3 = model.most_similar(u"好", topn=20)
    print("和【好】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")

    y3 = model.most_similar(u"不好", topn=20)
    print("和【不好】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")
    print(model["好"])

# model_test()

# result=wordsCluster()
# print(result)
