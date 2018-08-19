# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_56_MergeIntervals.py

@time: 2018/8/19 上午10:45

'''
def merge( intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    res = []
    for inter in sorted(intervals, key = lambda _:_[0]):
        print res
        if res and res[-1][1] >= inter[0]:
            res[-1][1] = max(inter[1], res[-1][1])
        else :
            # print inter
            res.append(inter)
    return res

if __name__ == '__main__':
    print merge([[1,4],[2,3]])

