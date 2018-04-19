# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_39_CombinationSum.py

@time: 2018/4/18 上午11:37

'''
def back(canlist,target, rightlist, res, step):
    if sum(rightlist) == target:
        #print rightlist
        res.append(rightlist[:])
        return

    for i in range(len(canlist)):
        if step <= i and canlist[i] + sum(rightlist) <= target:
            rightlist.append(canlist[i])
            back(canlist, target, rightlist, res, i)
            rightlist.pop()

def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    rightlist = []
    res = []
    step = 0
    back(candidates, target, rightlist, res, step)
    return res


if __name__ == '__main__':
    print combinationSum([2,3,5], 8)

