#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:speed_benchmark.py
# author:xm
# datetime:2023/11/6 13:15
# software: PyCharm

"""
2.3.5 速度评测
(1) 同等条件下, Python的运行速度比Java慢, 效率只有Java的一半不到
(2) 正向匹配和逆向匹配的速度差不多, 是双向的两倍. 这在意料之中, 因为双向匹配做了两倍的工作
(3) Java实现的正向匹配比逆向匹配快, 可能是内存回收的原因. 即便如此, 依然比Python快.

考虑到运行效率的差距, 建议Python用户使用Cython、C/C++动态链接库等机制实现生产环境中的核心算法, 或者直接使用JClass调用HanLP的Java接口
"""

# import module your need
import time

from ch02.backward_segment import backward_segment
from ch02.bidirectional_segment import bidirectional_segment
from ch02.forward_segment import forward_segment
from ch02.utility import load_dictionary


def evaluate_speed(segment, text, dic):
    start_time = time.time()
    for i in range(pressure):
        segment(text, dic)
    elapsed_time = time.time() - start_time
    print('%.2f 万字/秒' % (len(text) * pressure / 10000 / elapsed_time))


if __name__ == '__main__':
    text = "江西鄱阳湖干枯，中国最大淡水湖变成大草原"
    pressure = 10000
    dic = load_dictionary()

    print('由于JPype调用开销巨大，以下速度显著慢于原生Java')
    evaluate_speed(forward_segment, text, dic)
    evaluate_speed(backward_segment, text, dic)
    evaluate_speed(bidirectional_segment, text, dic)
