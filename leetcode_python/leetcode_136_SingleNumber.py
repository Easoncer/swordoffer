# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_136_SingleNumber.py

@time: 2018/4/2 下午1:29

'''


def singleNumber( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    return reduce(lambda x, y: x ^ y, nums)


if __name__ == '__main__':
    pass

