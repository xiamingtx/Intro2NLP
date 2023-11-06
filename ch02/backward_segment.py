#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:backward_segment.py
# author:xm
# datetime:2023/11/6 12:07
# software: PyCharm

"""
2.3.3 逆向最长匹配
"""

# import module your need
from ch02.utility import load_dictionary


def backward_segment(text, dic):
    word_list = []
    i = len(text) - 1
    while i >= 0:                                   # 扫描位置作为终点
        longest_word = text[i]                      # 扫描位置的单字
        for j in range(0, i):                       # 遍历[0, i]区间作为待查询词语的起点
            word = text[j: i + 1]                   # 取出[j, i]区间作为待查询单词
            if word in dic:
                if len(word) > len(longest_word):   # 越长优先级越高
                    longest_word = word
                    break
        word_list.insert(0, longest_word)           # 逆向扫描，所以越先查出的单词在位置上越靠后
        i -= len(longest_word)
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()

    print(backward_segment('研究生命起源', dic))  # ['研究', '生命', '起源']
    print(backward_segment('项目的研究', dic))   # ['项', '目的', '研究'] 这边出错了, 但是在forward_segment是正确的
