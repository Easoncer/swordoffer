# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_476_NumberComplement.py

@time: 2018/3/30 下午8:34

'''


def findComplement(num):
    numlen = '1' * (len(bin(num)) - 2)
    return int(numlen, 2)^num

if __name__ == '__main__':
    print findComplement(5)

