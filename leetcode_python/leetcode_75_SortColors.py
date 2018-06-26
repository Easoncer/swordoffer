# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_75_SortColors.py

@time: 2018/6/26 下午4:49

'''


class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        index = start

        while index <= end:
            if nums[index] == 0:
                nums[start], nums[index] = nums[index], nums[start]
                start += 1
                index += 1

            elif nums[index] == 2:
                nums[end], nums[index] = nums[index], nums[end]
                end -= 1
            else:
                index += 1

