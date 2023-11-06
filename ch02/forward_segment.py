#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:forward_segment.py
# author:xm
# datetime:2023/11/6 11:59
# software: PyCharm

"""
2.3.2 正向最长匹配
考虑到越长的单词表达的意义越丰富, 于是我们定义单词越长优先级越高.
具体来说就是在以某个下标为起点递增查词的过程中,优先输出更长的单词, 这周规则被称为最长匹配算法
该下表的扫描顺序如果从前往后, 则称正向最长匹配, 反之则称逆向最长匹配
"""

# import module your need
from ch02.utility import load_dictionary


def forward_segment(text, dic):
    word_list = []
    i = 0
    while i < len(text):
        longest_word = text[i]                      # 当前扫描位置的单字
        for j in range(i + 1, len(text) + 1):       # 所有可能的结尾
            word = text[i:j]                        # 从当前位置到结尾的连续字符串
            if word in dic:                         # 在词典中
                if len(word) > len(longest_word):   # 并且更长
                    longest_word = word             # 则更优先输出
        word_list.append(longest_word)              # 输出最长词
        i += len(longest_word)                      # 正向扫描
    return word_list


if __name__ == '__main__':
    dic = load_dictionary()

    print(forward_segment('就读北京大学', dic))   # ['就读', '北京大学']
    print(forward_segment('研究生命起源', dic))   # ['研究生', '命', '起源']
    print(forward_segment('项目的研究', dic))    # ['项目', '的', '研究']
