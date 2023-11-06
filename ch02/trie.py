#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:trie.py
# author:xm
# datetime:2023/11/6 13:30
# software: PyCharm

"""
2.4 字典树
"""


class Node(object):
    def __init__(self, value) -> None:
        self._children = {}
        self._value = value

    def _add_child(self, char, value, overwrite=False):
        # 检查是否已经存在字符char对应的child(None表示节点不对应词语)
        child = self._children.get(char)
        if child is None:
            child = Node(value)
            self._children[char] = child
        # 用overwrite来决定是否覆盖child的值
        elif overwrite:
            child._value = value
        return child


class Trie(Node):
    def __init__(self) -> None:
        super().__init__(None)

    def __contains__(self, key):
        return self[key] is not None

    def __getitem__(self, key):
        state = self
        for char in key:
            state = state._children.get(char)
            if state is None:
                return None
        return state._value

    def __setitem__(self, key, value):
        state = self
        for i, char in enumerate(key):
            # 对于这个key前缀部分, 要在trie树中add(保证存在)
            # '自然'    对'自' 如果不存在, 会增加一个'自', 但是value=None 表明并不存在'自'这个词语
            if i < len(key) - 1:
                state = state._add_child(char, None, False)
            # 对于结尾字符, 要进行overwrite
            # '自然'    对'然' 如果不存在, 会增加一个'然', 如果已存在就覆盖
            else:
                state = state._add_child(char, value, True)


if __name__ == '__main__':
    trie = Trie()
    # 增 调用__setitem__
    trie['自然'] = 'nature'
    trie['自然人'] = 'human'
    trie['自然语言'] = 'language'
    trie['自语'] = 'talk	to oneself'
    trie['入门'] = 'introduction'
    assert '自然' in trie
    # 删
    trie['自然'] = None
    assert '自然' not in trie
    # 改
    trie['自然语言'] = 'human language'
    assert trie['自然语言'] == 'human language'
    # 查
    assert trie['入门'] == 'introduction'
