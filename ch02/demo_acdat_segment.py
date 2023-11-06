#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:demo_acdat_segment.py
# author:xm
# datetime:2023/11/6 23:47
# software: PyCharm

"""
2.8 HanLP 的词典分词实现
"""

# import module your need
from pyhanlp import *

HanLP.Config.ShowTermNature = False  # 是否显示词性, 如果下面为True 这里也要设置为True才行
segment = JClass('com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment')(HanLP.Config.CoreDictionaryPath)
# segment.enablePartOfSpeechTagging(True) # 显示词性、进行数字英文的合并需要开启为True
print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))  # [江西, 鄱阳湖, 干枯, ，, 中国, 最大, 淡水湖, 变成, 大草原]
# for term in segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"):
#     print(f'单词: {term.word} 词性:  {term.nature}')
