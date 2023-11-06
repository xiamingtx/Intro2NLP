#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:dat.py
# author:xm
# datetime:2023/11/6 14:23
# software: PyCharm

"""
2.5 双数组字典树

字典树其实就是DFA, 双数组字典树依然是DFA, DFA中的状态由base与check中的元素和下标表示,
具体说来, 当状态b接受字符c转移到状态p时, 双数组满足:

p = base[b] + c
check[p] = base[b]

若不满足此条件, 则转移失败.
举个例子, 当前状态为'自然' (状态由一个数组下标表示, 下同), 我们想知道是否可以转移到'自然人'
那么我们先执行  自然人 = base[自然] + 人, 然后检查 check[自然人] = base[自然] 是否成立, 据此判断转移是否成功.
也就是说, 我们仅仅执行一次加法和一次整数比较就能进行状态转移, 因此只花费了常数时间.
"""

# import module your need
from pyhanlp import *


class DoubleArrayTrie(object):
    def __init__(self, dic: dict) -> None:
        m = JClass('java.util.TreeMap')()
        for k, v in dic.items():
            m[k] = v
        DoubleArrayTrie = JClass('com.hankcs.hanlp.collection.trie.DoubleArrayTrie')
        dat = DoubleArrayTrie(m)
        self.base = dat.getBase()
        self.check = dat.getCheck()
        self.value = dat.getValueArray([''])

    @staticmethod
    def char_hash(c) -> int:
        """
        Python默认的散列函数不适合字符, 我们可以借用Java的hashCode方法拿到了散列值
        :param c: 字符
        :return: hashcode
        """
        return JClass('java.lang.Character')(c).hashCode()

    def transition(self, c, b) -> int:
        """
        兼容\0的状态转移函数

        考虑到不是所有节点都对应词语终点, 只有字典树中的终点节点(蓝色节点)才对应一个词语. 为了区分它们, 实现上可以借鉴C语言中的设计, 在每个
        字符串末尾添加一个散列值等于0的\0. 也就是说, \0充当了蓝色节点的角色, 这样普通节点就不需要分配内存标记自己的颜色了.
        考虑到用户输入的文本中也可能含有\0, 为了避免与此混淆, 只需将文本字符的hashCode加一就行了.
        :param c: 字符
        :param b: 初始状态
        :return: 转移后的状态，-1表示失败
        """
        p = self.base[b] + self.char_hash(c) + 1
        if self.base[b] == self.check[p]:
            return p
        else:
            return -1

    def __getitem__(self, key: str):
        """
        有了转移函数, 对key的查询就是至多len(key) + 1次状态转移, 多出来的因此针对\0
        :param key:
        :return:
        """
        b = 0
        for i in range(0, len(key)):  # len(key)次状态转移
            p = self.transition(key[i], b)
            if p != -1:
                b = p
            else:
                return None

        p = self.base[b]  # 按字符'\0'进行状态转移
        n = self.base[p]  # 查询base
        if p == self.check[p] and n < 0:  # 状态转移成功且对应词语结尾
            index = -n - 1  # 取得字典序
            return self.value[index]
        return None


if __name__ == '__main__':
    dic = {'自然': 'nature', '自然人': 'human', '自然语言': 'language', '自语': 'talk	to oneself', '入门': 'introduction'}
    dat = DoubleArrayTrie(dic)
    assert dat['自然'] == 'nature'
    assert dat['自然语言'] == 'language'
    assert dat['不存在'] is None
    assert dat['自然\0在'] is None
