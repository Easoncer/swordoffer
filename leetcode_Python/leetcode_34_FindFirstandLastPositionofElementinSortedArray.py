# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_34_FindFirstandLastPositionofElementinSortedArray.py

@time: 2018/8/20 下午6:42

'''


def searchRange( nums, target, flag):
    """
    :type nums: List[int]
    :type target: int
    :rtype:
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] < target:
            left = mid + 1
        if nums[mid] > target:
            right = mid - 1
        # True left num
        if nums[mid] == target and flag:
            while  mid>=0 and nums[mid] == target:
                mid -= 1
            return mid+1
        if nums[mid] == target  and not flag:
            while mid <= len(nums)-1 and nums[mid] == target:
                mid += 1
            return mid-1
    return -1

if __name__ == '__main__':
    print searchRange([7,7,8,8,10], 3, True)
    print searchRange([7,7,8,8,10], 3, False)

