# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_70_ClimbingStairs.py

@time: 2018/4/18 下午12:24

'''


def climbStairs(n):
    """
    :type n: int
    :rtype: int
    """
    step = [0,1,2]
    for i in range(3,n+1):
        step.append(step[i-1]+step[i-2])
    return step[n]

if __name__ == '__main__':
    print climbStairs(3)

