# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_553_OptimalDivision.py

@time: 2018/4/2 下午2:04

'''


def optimalDivision( nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    if len(nums) == 1:
        return str(nums[0])
    if len(nums) == 2:
        return '%s/%s' % (str(nums[0]), str(nums[1]))
    return '%s/(%s)' % (str(nums[0]), '/'.join(map(str, nums[1:])))

if __name__ == '__main__':
    pass

