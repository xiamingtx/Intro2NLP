#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:fully_segment.py
# author:xm
# datetime:2023/11/6 11:53
# software: PyCharm

"""
2.3.1 完全切分
完全切分指的是找出一段文本中的所有单词
"""

# import module your need
from ch02.utility import load_dictionary


def fully_segment(text, dic):
    word_list = []
    for i in range(len(text)):                  # i 从 0 到text的最后一个字的下标遍历
        for j in range(i + 1, len(text) + 1):   # j 遍历[i + 1, len(text)]区间
            word = text[i:j]                    # 取出连续区间[i, j]对应的字符串
            if word in dic:                     # 如果在词典中，则认为是一个词
                word_list.append(word)
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()
    # ['商', '商品', '品', '和', '和服', '服', '服务', '务']
    print(fully_segment('商品和服务', dic))
