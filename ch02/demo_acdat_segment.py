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

HanLP.Config.ShowTermNature = False
segment = JClass('com.hankcs.hanlp.seg.Other.AhoCorasickDoubleArrayTrieSegment')(HanLP.Config.CoreDictionaryPath)
print(segment.seg("江西鄱阳湖干枯，中国最大淡水湖变成大草原"))
