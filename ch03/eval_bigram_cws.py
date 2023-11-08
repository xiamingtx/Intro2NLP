#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:eval_bigram_cws.py
# author:xm
# datetime:2023/11/8 13:03
# software: PyCharm

"""
3.5.1 标准化评测
"""

# import module your need
from pyhanlp import *
from ch03.msr import msr_dict, msr_train, msr_model, msr_test, msr_output, msr_gold
from ch03.ngram_segment import train_bigram, load_bigram

CWSEvaluator = SafeJClass('com.hankcs.hanlp.seg.common.CWSEvaluator')

if __name__ == '__main__':
    train_bigram(msr_train, msr_model)  # 训练
    segment = load_bigram(msr_model)  # 加载
    result = CWSEvaluator.evaluate(segment, msr_test, msr_output, msr_gold, msr_dict)  # 预测打分
    print(result)
