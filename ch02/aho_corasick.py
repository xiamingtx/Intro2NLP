#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:aho_corasick.py
# author:xm
# datetime:2023/11/6 23:20
# software: PyCharm

"""
2.6 AC 自动机
Trie + KMP
"""

# import module your need
from pyhanlp import *


def classic_demo():
    words = ["hers", "his", "she", "he"]
    Trie = JClass('com.hankcs.hanlp.algorithm.ahocorasick.trie.Trie')
    trie = Trie()
    for w in words:
        trie.addKeyword(w)

    for emit in trie.parseText("ushers"):
        print("[%d:%d]=%s" % (emit.getStart(), emit.getEnd(), emit.getKeyword()))


if __name__ == '__main__':
    classic_demo()
