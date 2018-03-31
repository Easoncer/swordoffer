# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_575_DistributeCandies.py

@time: 2018/3/31 下午4:35

'''
def distributeCandies( candies):
    return min(len(candies) / 2, len(set(candies)))

if __name__ == '__main__':
    print distributeCandies([1,1,2,2,3,3])

