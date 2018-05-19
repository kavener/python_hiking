from gensim.models import Word2Vec
import variable_id
import get_comments as gc
import pretreatment as ptt
import participle as ple
import delete_stop_word as dsw
import build_word2vec as bd2
import create_wordCloud as cwd
import kmeans as ks

product_ID = 4609652
product_ID = 5001209
product_ID = 5089237
product_ID = 5089253

fh = open("./variable_id.py", "w")
fh.write("semaphore=0" + "\n")
fh.write("product_id=" + str(product_ID))
fh.close()


def Go():
    gc.get_comments()
    ptt.pretreatment_id()
    ple.participle_id()
    dsw.stop_word_id()
    cwd.creat_worldCloud_id()
    bd2.build_word2vec_id()
    ks.kmeans_id()


def model_test():
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


Go()

# model_test()
