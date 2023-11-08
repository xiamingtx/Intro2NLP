#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:adjust_model.py
# author:xm
# datetime:2023/11/8 13:06
# software: PyCharm

"""
3.5.3 调整模型
"""

# import module your need
from pyhanlp import HanLP
from ch03.msr import msr_model
from ch03.ngram_segment import load_bigram, CoreDictionary

segment = load_bigram(model_path=msr_model, verbose=False, ret_viterbi=False)
assert CoreDictionary.contains("管道")
text = "北京输气管道工程"
HanLP.Config.enableDebug()
print(segment.seg(text))
