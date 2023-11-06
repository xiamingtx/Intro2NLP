#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:bidirectional_segment.py
# author:xm
# datetime:2023/11/6 13:09
# software: PyCharm

"""
双向最长匹配流程如下:
(1) 同时执行正向和逆向最长匹配, 若两者的词数不同, 则返回词数更少的哪一个
(2) 否则, 返回两者中单字更少的那一个. 当单字数也相同时, 优先返回逆向最长匹配的结果
"""

# import module your need
from ch02.backward_segment import backward_segment
from ch02.forward_segment import forward_segment
from ch02.utility import load_dictionary


def count_single_char(word_list: list):  # 统计单字成词的个数
    return sum(1 for word in word_list if len(word) == 1)


def bidirectional_segment(text, dic):
    f = forward_segment(text, dic)
    b = backward_segment(text, dic)
    if len(f) < len(b):                                  # 词数更少优先级更高
        return f
    elif len(f) > len(b):
        return b
    else:
        if count_single_char(f) < count_single_char(b):  # 单字更少优先级更高
            return f
        else:
            return b                                     # 都相等时逆向匹配优先级更高


if __name__ == '__main__':
    dic = load_dictionary()

    print(bidirectional_segment('研究生命起源', dic))  # ['研究', '生命', '起源']   √
    print(bidirectional_segment('项目的研究', dic))  # ['项', '目的', '研究']     ×
