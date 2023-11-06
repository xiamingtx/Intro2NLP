#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:utility.py
# author:xm
# datetime:2023/11/6 11:32
# software: PyCharm

"""
2.2.2 词典的加载
"""

# import module your need
from pyhanlp import *


def load_dictionary():
    """
    加载HanLP中的mini词库
    :return: 一个set形式的词库
    """
    IOUtil = JClass('com.hankcs.hanlp.corpus.io.IOUtil')  # JClasss是连通Java和Python的桥梁, 根据Java路径名得到一个Python类
    path = HanLP.Config.CoreDictionaryPath.replace('.txt', '.mini.txt')
    dic = IOUtil.loadDictionary([path])
    return set(dic.keySet())


if __name__ == '__main__':
    dic = load_dictionary()
    print(len(dic))
    print(list(dic)[0])
