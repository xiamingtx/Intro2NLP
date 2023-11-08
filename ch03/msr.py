#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:msr.py
# author:xm
# datetime:2023/11/8 11:05
# software: PyCharm

"""
3.2.2 微软亚洲研究院语料库 MSR
"""

# import module your need
import os

from test_utility import ensure_data, test_data_path

sighan05 = ensure_data('icwb2-data', 'http://sighan.cs.uchicago.edu/bakeoff2005/data/icwb2-data.zip')
msr_dict = os.path.join(sighan05, 'gold', 'msr_training_words.utf8')
msr_train = os.path.join(sighan05, 'training', 'msr_training.utf8')
msr_model = os.path.join(test_data_path(), 'msr_cws')
msr_test = os.path.join(sighan05, 'testing', 'msr_test.utf8')
msr_output = os.path.join(sighan05, 'testing', 'msr_bigram_output.txt')
msr_gold = os.path.join(sighan05, 'gold', 'msr_test_gold.utf8')