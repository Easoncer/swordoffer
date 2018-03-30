# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_557_ReverseWordsinaString III.py

@time: 2018/3/30 下午10:19

'''


def reverseWords( s):
    """
    :type s: str
    :rtype: str
    """
    return ' '.join([i[::-1] for i in s.split(' ')])


if __name__ == '__main__':
    pass

