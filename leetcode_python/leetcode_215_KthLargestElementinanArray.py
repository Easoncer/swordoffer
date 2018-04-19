# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_215_KthLargestElementinanArray.py

@time: 2018/4/19 下午12:47

'''
def partition(nums, left, right):
    i = left
    key = nums[right]

    for j in range(left, right):
        if nums[j] < key:
            nums[i], nums[j]= nums[j], nums[i]
            i += 1
    nums[i], nums[right] = key, nums[i]
    return i


def quicksort(nums,left,right,k):
    if left < right:
        temp = partition(nums, left, right)
        if k == right-temp+1 :
            return
        elif k < right-temp+1:
            quicksort(nums, temp + 1, right,k)
        else:
            k -= right -temp+1
            quicksort(nums, left, temp-1,k)

def findKthLargest( nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    quicksort(nums, 0, len(nums)-1,k)
    print nums[-1*k]


if __name__ == '__main__':
    nums = [3,2,1,5,6,4,5.5]
    k =  2
    findKthLargest(nums, k)
