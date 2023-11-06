#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:aho_corasick_double_array_trie.py
# author:xm
# datetime:2023/11/6 23:43
# software: PyCharm

"""
2.7 基于双数组字典树的 AC 自动机
"""

# import module your need
from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    map = JClass('java.util.TreeMap')()     # 创建TreeMap实例
    for word in words:
        map[word] = word.upper()            # 存放键值对
    trie = JClass('com.hankcs.hanlp.collection.AhoCorasick.AhoCorasickDoubleArrayTrie')(map)
    for hit in trie.parseText("ushers"):    # 遍历查询结果
        print("[%d:%d]=%s" % (hit.begin, hit.end, hit.value))


if __name__ == '__main__':
    classic_demo()
