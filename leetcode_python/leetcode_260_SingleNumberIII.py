# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_260_SingleNumberIII.py

@time: 2018/4/3 下午12:53

'''


def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = reduce(lambda x, y: x ^ y, nums)
    num = 1 << (len(bin(res)[2:]) - 1)
    num1 = reduce(lambda x, y: x ^ y, filter(lambda _: _ & num > 0, nums))
    num2 = reduce(lambda x, y: x ^ y, filter(lambda _: _ & num == 0, nums))
    return [num1, num2]

if __name__ == '__main__':
    pass

