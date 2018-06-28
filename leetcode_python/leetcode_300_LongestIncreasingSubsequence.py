# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_300_LongestIncreasingSubsequence.py

@time: 2018/6/28 上午10:37

'''


def lengthOfLIS( nums ):
    """
    :type nums: List[int]
    :rtype: int
    """

    '''
      O(n^2)
    '''
    # if len(nums) == 0:
    #     return 0
    # res = 1
    # templist = [1]
    # for i in range(1, len(nums)):
    #     temp = 1
    #     for j in range(i):
    #         if nums[i] > nums[j]:
    #             temp = max(temp, templist[j]+1)
    #     res = max(temp, res)
    #     templist.append(temp)
    #
    # return res

    '''
        O(n lg n)
    '''

    if len(nums) == 0:
        return 0
    templist = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] > templist[-1]:
            templist.append(nums[i])

        else:
            # two division
            start, end = 0, len(templist)-1

            while start < end:
                mid = (start+end)/2

                if templist[mid] < nums[i]:
                    start = mid + 1

                if templist[mid] >= nums[i]:
                    end = mid

            templist[end] = nums[i]
    return templist



def sorted_(templist ,key):

    start, end = 0, len(templist) - 1

    while start < end:
        mid = (start + end) / 2

        if templist[mid] < key:
            start = mid + 1

        if templist[mid] >= key:
            end = mid
    templist[end] = key
    return  templist

if __name__ == '__main__':
    print lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12])
    #print sorted_([3,3,5,7,8], 3)
