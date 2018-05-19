inputFile = "./../useful/stop_word.txt"
outputFile = "./../useful/structure_filter_words.txt"

data = open(inputFile).readlines()
print(data)
data_with_parameter = ''
data_with_parametered = ''
# 使用循环添加参数为结巴认可的词典格式
'''
for word in data:
    if (word=="\n" or word==" " or word=='\\' or word=="n" or word=="t"):
        continue
    words=word+" 3 stop_word"
    data_with_parameter.append(words)




'''
pat = '|&hellip;|&ldquo;|&rdquo;|&deg;|&times;|&mdash;|&quot;|&there4;|&omega;|&yen;|！|，|。|？|～|（|）|http://.*?none|!|!|\.|`|\?|@|#|%|^|&|\*|(\|)|,'

for stop_word in data:
    for str in stop_word:
        if (str != '\\' and str != 'n' and str != ' '):
            data_with_parameter += str
        else:
            data_with_parameter += '|'
            continue

# 写入文件构建词典
fh = open(outputFile, "w")
for i in data_with_parameter:
    # i=i.decode('utf-8').encode('gb2312')
    if (i == '\n'):
        continue
    else:
        print(i)
        fh.write(i)
    # print(i)
for pat_i in pat:
    if (i == '\n'):
        continue
    else:
        print(pat_i)
        fh.write(pat_i)
fh.close()
