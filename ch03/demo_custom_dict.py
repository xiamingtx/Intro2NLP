#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:demo_custom_dict.py
# author:xm
# datetime:2023/11/8 12:51
# software: PyCharm

"""
3.4.5 与用户词典的集成
"""

# import module your need
from pyhanlp import *

ViterbiSegment = SafeJClass('com.hankcs.hanlp.seg.Viterbi.ViterbiSegment')

segment = ViterbiSegment()
sentence = "社会摇摆简称社会摇"
segment.enableCustomDictionary(False)
print("不挂载词典：", segment.seg(sentence))
CustomDictionary.insert("社会摇", "nz 100")
segment.enableCustomDictionary(True)
print("低优先级词典：", segment.seg(sentence))
segment.enableCustomDictionaryForcing(True)
print("高优先级词典：", segment.seg(sentence))
