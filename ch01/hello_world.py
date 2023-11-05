#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:hello_world.py
# author:xm
# datetime:2023/11/5 20:27
# software: PyCharm

"""
this is function  description 
"""

# import module your need
from pyhanlp import *


def main():
    HanLP.Config.enableDebug()
    print(HanLP.segment("王国维和服务员"))  # [王国维/nr, 和/cc, 服务员/nnt]


if __name__ == '__main__':
    main()
