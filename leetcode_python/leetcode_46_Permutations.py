# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_46_Permutations.py

@time: 2018/4/5 下午4:27

'''
def backtrack(res, step, nums, mark, num_real ):
    if step == len(nums):
        res.append(nums[:])
        #print res
        return

    for i in range(len(nums)):
        if mark[i] == 0:
            mark[i] = 1
            nums[step] = num_real[i]
            backtrack(res, step+1, nums, mark,num_real )
            mark[i] = 0


def permute( num):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    mark = [0]*len(num)
    res = []
    backtrack(res, step=0, nums = num , mark= mark, num_real = num[:])
    return res


if __name__ == '__main__':
    print permute([1,3])

