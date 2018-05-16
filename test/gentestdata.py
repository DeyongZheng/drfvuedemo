#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, random
from datetime import date, timedelta
import numpy as np
import itertools

LASTNAME = [
    '佐藤','鈴木','高橋','田中','伊藤','渡辺','山本','中村','小林','加藤',
    '吉田','山田','佐々木','山口','松本','井上','木村','林','斎藤','清水',
    '山崎','森','池田','橋本','阿部','石川','山下','中島','石井','小川',
    '前田','岡田','長谷川','藤田','後藤','近藤','村上','遠藤','青木','坂本',
    '斉藤','福田','太田','西村','藤井','岡本','藤原','金子','三浦','中野',
    '中川','原田','松田','竹内','小野','田村','中山','和田','石田','森田',
    '上田','原','内田','柴田','酒井','宮崎','横山','高木','安藤','宮本',
    '大野','小島','工藤','谷口','今井','高田','増田','丸山','杉山','村田',
    '大塚','新井','藤本','小山','平野','河野','上野','武田','野口','松井',
    '千葉','菅原','岩崎','久保','木下','佐野','野村','松尾','菊地','杉本',
]

FIRSTNAME = [
    '大翔', '陽葵', '蓮', '葵', '樹', '陽菜', '悠真', '結衣', '陽太', '凛', 
    '蒼', '咲良', '結菜', '湊', '颯真', '結愛', '陽翔', '陽斗', '心春', '杏', 
    '紬', '奏太', '朝陽', '莉子', '芽依', '颯太', '岳', '凜', '悠斗', '結翔', 
    'さくら', '美月', 'あかり', '澪', '碧', '大和', '陽大', '悠人', '奏汰', 
    '悠', '楓', 'ひかり', '結月', '芽生', '悠翔', '瑛太', '陽向', '咲希', '琴音',
    'ひまり', '悠生', '颯', '翔太', '莉央', '彩葉', '花', '琴葉', '心結', '翔', 
    '新', '歩', '葵', '美桜', '心晴', '杏奈', '美咲', '桜', '柚希', '蒼太', '大智',
    '陸', '陽', '絢斗', '美結', '莉緒', '愛莉', '結', '心陽', '旭', '蒼士', '結斗', 
    '奏多', '碧斗', '華', '美織', '栞奈', '匠', '悠希', '遥斗', '颯人', '栞', 
    '朱莉', '優奈', '彩羽', '和奏', '晴', '蒼真', '湊太', '壮真', 'ひな', 
]

#生徒データの生成
def genstudents(filename):
    fo = open(filename, "w")
    for x in itertools.product(LASTNAME, FIRSTNAME):
        fo.writelines("{0},{1}\n".format(x[0], x[1]))
    fo.close()

#重複なしランタイム数字の生成
def gennum(min, max, count):
    return random.sample(range(min, max + 1), count)

def genhistory(filename, days = 10):
    now = date.today()
    dateList = []
    for x in range(0, days):
        dateList.append(now- timedelta(days = x))
    dateList.reverse()

    fo = open(filename, "w")
    for learningdate in dateList:
        students = gennum(1, 10000, 2000)
	students.sort()
	questions = np.random.normal(60, 25, 2000).astype(int)
	accuracies = np.random.normal(0.7, 0.15, 2000)

	for i in range(len(students)):
	    question = questions[i] if questions[i] > 0 else 0
	    accuracy = int(question * accuracies[i])
	    accuracy = accuracy if accuracy > 0 else 0
	    minutes = random.randint(1, 240)
	    fo.writelines("{0:%Y-%m-%d}, {1}, {2}, {3}, {4}\n".format(learningdate, students[i], question, accuracy, minutes))
    fo.close()
    

def main():
    reload(sys)
    sys.setdefaultencoding('utf-8')

    genstudents("students.csv")

    genhistory("history.csv", 10)

if __name__ == '__main__':
    main()
