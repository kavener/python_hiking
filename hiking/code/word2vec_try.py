from gensim.models import word2vec
from gensim.models import Word2Vec
from gensim.models import KeyedVectors


# word_vectors = KeyedVectors.load_word2vec_format('/tmp/vectors.txt', binary=False)  # C text format
# word_vectors = KeyedVectors.load_word2vec_format('/tmp/vectors.bin', binary=True)  # C binary format
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
    sentences = comments_to_comment()
    model = word2vec.Word2Vec(sentences, size=200)
    # model.save("./../data/model.txt")
    # model.save_word2vec_format("./../data/comments.model.bin", binary=True)
    model.wv.save_word2vec_format("./../data/comments.model.bin", binary=True)
    print(model)


def model_test():
    # model = Word2Vec.load("./../data/comments.model")
    model = KeyedVectors.load_word2vec_format("./../data/comments.model.bin", binary=True)
    # word_vectors = KeyedVectors.load_word2vec_format('/tmp/vectors.txt', binary=False)  # C text format
    # word_vectors = KeyedVectors.load_word2vec_format('./../data/model', binary=True)  # C binary format
    print(model)

    try:
        y1 = model.similarity(u"手机", "苹果")
    except KeyError:
        y1 = 0
    print("【手机】和【苹果】的相似度为：", y1)
    ss = '好'
    y3 = model.most_similar(ss, topn=20)
    print("和【" + ss + "】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")
    ss = '不好'
    y3 = model.most_similar(ss, topn=20)
    print("和【" + ss + "】最相关的词有：\n")
    for item in y3:
        print(item[0], item[1])
    print("------\n")


build_word2vec()
model_test()
