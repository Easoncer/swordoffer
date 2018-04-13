# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_78_Subsets.py

@time: 2018/4/8 下午8:57

'''
def backiter(step, nums, temp, res):
    res.append(temp[:])

    for i in range(step, len(nums)):
        temp.append(nums[i])
        backiter(i+1, nums, temp, res)
        temp.pop()


def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    step = 0
    res = []
    temp = []
    backiter(step, nums, temp, res)
    return res

if __name__ == '__main__':
    print subsets([1,2,3])

