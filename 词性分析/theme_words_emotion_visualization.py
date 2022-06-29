import csv
import matplotlib.pyplot as plt

positive_theme_emotion_count_SIZE = 80  # 设置正面倾向主题词出现次数，只有高于此次数的数据才会被统计
negative_theme_emotion_count_SIZE = 5  # 设置负面倾向主题词出现次数，只有高于此次数的数据才会被统计
table_x_SIZE = 40  # 设置显示情感值前多少个的正面/负面倾向主题词


# 统计主题词平均情感值，mode若为"positive"，统计正面倾向主题词；mode若为"negative"，统计负面倾向主题词
def getAvgThemeEmotionList(path, mode="positive"):
    csv_reader = csv.reader(open(path, encoding='gb18030'))
    theme_emotion_dict = {}  # 记录每个主题词对应总情感值
    theme_count_dict = {}  # 记录每个主题词出现次数

    for row in csv_reader:
        theme_words_list = row[2].split(';')  # 读取主题词列表
        emotion_list = row[4].split(';')  # 读取情感值列表
        for i in range(len(theme_words_list)):
            if theme_words_list[i] in theme_emotion_dict:  # 主题词存在，累加情感值
                theme_emotion_dict[theme_words_list[i]] += int(emotion_list[i])
                theme_count_dict[theme_words_list[i]] += 1
            else:  # 主题词不存在，加入词典
                if theme_words_list[i] != "NULL" and len(theme_words_list[i]) > 0:
                    theme_emotion_dict[theme_words_list[i]] = int(emotion_list[i])
                    theme_count_dict[theme_words_list[i]] = 1
    # 利用之前统计的词典创建主题词-情感值对应列表
    theme_emotion_list = []
    if mode == "positive":
        for key in theme_emotion_dict:
            if theme_count_dict[key] > positive_theme_emotion_count_SIZE and theme_emotion_dict[key] > 0:
                theme_emotion_dict[key] = theme_emotion_dict[key] / theme_count_dict[key]
                theme_emotion_list.append([key, theme_emotion_dict[key]])
        theme_emotion_list.sort(key=sortByValue, reverse=True)
    elif mode == "negative":
        for key in theme_emotion_dict:
            if theme_count_dict[key] > negative_theme_emotion_count_SIZE and theme_emotion_dict[key] < 0:
                theme_emotion_dict[key] = theme_emotion_dict[key] / theme_count_dict[key]
                theme_emotion_list.append([key, theme_emotion_dict[key]])
        theme_emotion_list.sort(key=sortByValue)

    return theme_emotion_list


# 统计主题词总情感值，mode若为"positive"，统计正面倾向主题词；mode若为"negative"，统计负面倾向主题词
# def getSumThemeEmotionList(path, mode="positive"):
#     csv_reader = csv.reader(open(path, encoding='gb18030'))
#     theme_emotion_dict = {}  # 记录每个主题词对应总情感值
#     theme_count_dict = {}  # 记录每个主题词出现次数
#
#     for row in csv_reader:
#         theme_words_list = row[2].split(';')  # 读取主题词列表
#         emotion_list = row[4].split(';')  # 读取情感值列表
#         for i in range(len(theme_words_list)):
#             if theme_words_list[i] in theme_emotion_dict:  # 主题词存在，累加情感值
#                 theme_emotion_dict[theme_words_list[i]] += int(emotion_list[i])
#                 theme_count_dict[theme_words_list[i]] += 1
#             else:  # 主题词不存在，加入词典
#                 if theme_words_list[i] != "NULL" and len(theme_words_list[i]) > 0:
#                     theme_emotion_dict[theme_words_list[i]] = int(emotion_list[i])
#                     theme_count_dict[theme_words_list[i]] = 1
#     # 利用之前统计的词典创建主题词-情感值对应列表
#     theme_emotion_list = []
#     if mode == "positive":
#         for key in theme_emotion_dict:
#             if theme_count_dict[key] > positive_theme_emotion_count_SIZE and theme_emotion_dict[key] > 0:
#                 theme_emotion_list.append([key, theme_emotion_dict[key]])
#         theme_emotion_list.sort(key=sortByValue, reverse=True)
#     elif mode == "negative":
#         for key in theme_emotion_dict:
#             if theme_count_dict[key] > negative_theme_emotion_count_SIZE and theme_emotion_dict[key] < 0:
#                 theme_emotion_list.append([key, theme_emotion_dict[key]])
#         theme_emotion_list.sort(key=sortByValue)
#
#     return theme_emotion_list


def sortByValue(Map):  # 按值排序
    return Map[1]


def visualization(theme_emotion_list):  # 可视化
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    x_list = []
    y_list = []
    color = []

    for e in theme_emotion_list:
        x_list.append(e[0])
        y_list.append(e[1])

        if e[1] > 0:
            color.append((0, e[1] * e[1], 0.5))
        else:
            color.append((e[1] * e[1], 0, 0.5))

    plt.figure(figsize=(25, 10))
    plt.xticks(size=10, rotation=30)
    plt.bar(x_list, y_list, color=color)
    for _x, _y in zip(x_list, y_list):
        plt.text(_x, _y + 0.02, '%.2f' % _y, ha='center', va='bottom', size=8)
    plt.show()


if __name__ == "__main__":
    avg_theme_emotion_list_positive = getAvgThemeEmotionList("result1.csv", "positive")
    avg_theme_emotion_list_negative = getAvgThemeEmotionList("result1.csv", "negative")
    avg_theme_emotion_list_merged = avg_theme_emotion_list_positive + avg_theme_emotion_list_negative[::-1]

    visualization(avg_theme_emotion_list_merged)
    visualization(avg_theme_emotion_list_negative)
    visualization(avg_theme_emotion_list_positive)

