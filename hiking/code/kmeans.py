import codecs
import nltk
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import variable_id as vbs


def wordsCluster():
    classCount = 10

    model = Word2Vec.load("./../data/comments.model")
    # 获取所有关键词
    keys = model.wv.vocab.keys()
    # 获取关键词对应词向量
    wordvector = []
    reKeys = []
    for key in keys:
        wordvector.append(model[key])
        reKeys.append(key)
    # 聚类
    clf = KMeans(n_clusters=classCount)
    s = clf.fit(wordvector)
    print(s)
    # 获取所有词向量所属类别
    labels = clf.labels_
    print("----------------")
    # 利用集合把是一类的放到一个列表中
    # 创建一个对应字典：
    classCollects = {}
    for key_number in range(0, classCount):
        classCollects[key_number] = []

    for i in range(len(keys)):
        classCollects[labels[i]].append(reKeys[i])

    return classCollects


def kmeans_keys():
    s = wordsCluster()
    number = 1
    # print(s)
    fh = open("./../data/clustering_result.txt", "w")
    for number in range(0, len(s)):
        numbers = number + 1
        fh.write("第" + str(numbers) + "类聚类结果：\n")
        for word in s[number]:
            fh.write(str(word) + "\n")
        number += 1
    fh.write(str(s))
    fh.close()

    # print(s[0])
    # print(len(s))

    for i in range(0, len(s)):
        j = i + 1
        print("第 " + str(j) + " 类聚类结果:")
        for j in s[i]:
            print(j)


# kmeans_keys()
def kmeans_id():
    while True:
        if vbs.semaphore == 6:
            print("kmeans聚类...")
            kmeans_keys()
            break
    print("kmeans聚类完成.")
    vbs.semaphore = 7