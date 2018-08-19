# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_33_SearchinRotatedSortedArray.py

@time: 2018/8/19 下午12:15

'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        start = 0
        end = len(nums) - 1

        while start <= end:

            mid = (start + end) / 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[start]:  # 当nums[mid]属于左边升序序列时

                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            if nums[mid] < nums[end]:  # 当nums[mid]属于右边升序序列时

                if target > nums[mid] and target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1


if __name__ == '__main__':
    print search([3,1], 0)

