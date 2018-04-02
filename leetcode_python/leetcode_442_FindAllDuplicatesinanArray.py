# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_442_FindAllDuplicatesinanArray.py

@time: 2018/4/1 下午9:10

'''


def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for i in nums:
        if nums[abs(i) - 1] < 0:
            res.append(abs(i))
        else:
            nums[abs(i) - 1] *= -1
    return res

if __name__ == '__main__':
    pass

