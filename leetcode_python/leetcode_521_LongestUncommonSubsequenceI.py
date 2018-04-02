# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_521_LongestUncommonSubsequenceI.py

@time: 2018/4/2 上午10:58

'''


def findLUSlength( a, b):
    """
    :type a: str
    :type b: str
    :rtype: int
    """
    return -1 if a == b else max(len(a), len(b))

if __name__ == '__main__':
    pass

