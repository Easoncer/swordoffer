# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_693_BinaryNumberwithAlternatingBits.py

@time: 2018/4/2 上午11:07

'''


def hasAlternatingBits( n):
    """
    :type n: int
    :rtype: bool
    """
    num = (n>>1) ^ n

    return False if (num+1)&num  else True
if __name__ == '__main__':
    print hasAlternatingBits(7)

