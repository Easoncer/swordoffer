# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_287_FindtheDuplicateNumber.py

@time: 2018/4/8 下午9:20

'''


def findDuplicate( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in nums:
        if nums[abs(i)] > 0:
            nums[abs(i)] *= -1
        else:
            return abs(i)

if __name__ == '__main__':
    print findDuplicate([1,2,3,4,3])

