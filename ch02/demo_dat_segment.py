#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:demo_dat_segment.py
# author:xm
# datetime:2023/11/7 11:06
# software: PyCharm

"""
2.8 HanLP 的词典分词实现
"""

# import module your need
from pyhanlp import *
from pyhanlp.static import HANLP_DATA_PATH

HanLP.Config.ShowTermNature = False
dict1 = HANLP_DATA_PATH + "/dictionary/CoreNatureDictionary.mini.txt"
dict2 = HANLP_DATA_PATH + "/dictionary/custom/上海地名.txt ns"

segment = DoubleArrayTrieSegment(dict1)
print(segment.seg('江西鄱阳湖干枯，中国最大淡水湖变成大草原'))

segment = DoubleArrayTrieSegment([dict1, dict2])
print(segment.seg('上海市虹口区大连西路550号SISU'))

segment.enablePartOfSpeechTagging(True)
HanLP.Config.ShowTermNature = True
print(segment.seg('上海市虹口区大连西路550号SISU'))

for term in segment.seg('上海市虹口区大连西路550号SISU'):
    print("单词:%s 词性:%s" % (term.word, term.nature))
