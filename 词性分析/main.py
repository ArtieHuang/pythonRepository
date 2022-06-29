import csv


def getEmotion(negPath,posPath,neuPath,ignPath):
    neg_reader=csv.reader(open(negPath))
    pos_reader=csv.reader(open(posPath))
    neu_reader=csv.reader(open(neuPath))
    ign_reader=csv.reader(open(ignPath))

    negwords = []
    poswords = []
    neuwords = []
    ignwords = []

    for word in neg_reader:
        negwords.append(str(word[0]))
    for word in pos_reader:
        poswords.append(str(word[0]))
    for word in neu_reader:
        neuwords.append(str(word[0]))
    for word in ign_reader:
        ignwords.append(str(word[0]))

    return negwords,poswords,neuwords,ignwords



def checkEmotion(trainingDataPath,testingDataPath,negative,positive,nutral,ignore):
    result=open("result.csv",'w',newline='')
    writer=csv.writer(result,dialect='excel')
    reader=csv.reader(open(testingDataPath))
    for row in reader:
        words=row[0]; #句子在测试集的哪一列
        cutwordAndTagging = []  # 保存切分好的词及其词性
        emotionwordsAndtag = []  # 保存情感词及其词性和情感值
        themewords = []  # 情感词对应的主题词
        for word, flag in words:
            if word not in stopwords:  # 去除停用词之后切好的词，现在需要筛选出情感词
                cutwordAndTagging.append([word, flag])
        for wordAndtag in cutwordAndTagging:
            if wordAndtag[0] in positivewords:  # 如果在正向词内
                list = wordAndtag
                list.append(1)
                emotionwordsAndtag.append(list)
            elif wordAndtag[0] in negativewords:  # 如果在负向词内
                list = wordAndtag
                list.append(-1)
                emotionwordsAndtag.append(list)
            elif wordAndtag[0] in Neutralwords:  # 如果在中性词内
                list = wordAndtag
                list.append(0)
                emotionwordsAndtag.append(list)
        for word in emotionwordsAndtag:
            count = 0
            for wordlist in cutwordAndTagging:
                if (word[0] == wordlist[0]):
                    break
                count += 1
            if (count == 0):  # 第一个情感词，主题为null
                themewords.append("NULL")
            else:  # 找到该情感词前面一个n或者nr或者nt或者vn或者ns的词作为主题词
                if (cutwordAndTagging[count - 1][1] == 'n' or cutwordAndTagging[count - 1][1] == 'nt' or
                        cutwordAndTagging[count - 1][1] == 'nr'
                        or cutwordAndTagging[count - 1][1] == 'vn' or cutwordAndTagging[count - 1][1] == 'ns' or
                        cutwordAndTagging[count - 1][1] == 'nz' or cutwordAndTagging[count - 1][1] == 'nrt'):
                    themewords.append(cutwordAndTagging[count - 1][0])
                else:
                    themewords.append("NULL")
        list = []
        list.append(row[0])  # row_id
        list.append(row[1])  # content
        newthemewords = ""
        newsentimentwords = ""
        newsentimentanls = ""
        tem = []
        for i in range(len(themewords)):
            themeAndsentimentword = []
            themeAndsentimentword.append(themewords[i])  # 主题词
            themeAndsentimentword.append(emotionwordsAndtag[i][0])  # 情感词
            themeAndsentimentword.append(emotionwordsAndtag[i][2])  # 情感值
            if themeAndsentimentword not in tem:
                tem.append(themeAndsentimentword)
        # print(tem)
        for line in tem:
            newthemewords = newthemewords + str(line[0]) + ";"
            newsentimentwords = newsentimentwords + str(line[1]) + ";"
            newsentimentanls = newsentimentanls + str(line[2]) + ";"
        list.append(newthemewords)
        list.append(newsentimentwords)
        list.append(newsentimentanls)

        # print(list)
        csv_writer.writerow(list)



def cut(line):
    lac = LAC(mode='lac')
    line = re.sub(re.compile(r'[^\u4e00-\u9fa5]'), "", line)
    return lac.run(line)

if __name__ == '__main__':
    negativePath = "Data/negative.txt"
    positvePath = "Data/positive.txt"
    neutralPath="Data/neutral.txt"
    ignorePath="Data/ignore.txt"
    negative, positive, neutral,ignore = getEmotion(negativePath,positvePath,neutralPath,ignorePath)



    trainingDataPath="TrainingData/TrainingDataSet.csv"
    testingDataPath="TestingData/testingdata.csv"

    checkEmotion(trainingDataPath,testingDataPath,negative,positive,neutral,ignore)
