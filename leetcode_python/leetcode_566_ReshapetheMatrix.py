# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_566_ReshapetheMatrix.py

@time: 2018/3/31 下午5:50

'''


def matrixReshape(self, nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    if r * c != len(nums) * len(nums[0]):
        return nums
    temp = []
    for i in nums:
        temp.extend(i)
    re = []
    for i in range(r):
        re.append(temp[i * c:(i + 1) * c])
    return re

if __name__ == '__main__':
    pass

