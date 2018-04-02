# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_540_SingleElementinaSorted Array.py

@time: 2018/4/1 下午9:39

'''


def singleNonDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # the first method

    # return reduce(lambda x, y: x ^ y, nums)
    #how to use the sorted method
    # the sorted array , we can use the two division method
    low = 0
    high = len(nums) - 1
    while low < high:

        middle = (low + high) / 2

        if nums[middle] == nums[middle + 1]:
            if middle % 2 == 0:
                low = middle + 2
            else:
                high = middle - 1
            if high - low == 2:
                return nums[middle - 1]

        elif nums[middle] == nums[middle - 1]:
            if middle % 2 == 0:
                high = middle - 2
            else:
                low = middle + 1
            if high - low == 2:
                return nums[middle + 1]

        else:
            return nums[middle]


if __name__ == '__main__':
    print singleNonDuplicate([2,1,1,3,3,4,4,8,8])

