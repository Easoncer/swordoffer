# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_121_BestTimetoBuyandSellStock.py

@time: 2018/4/13 上午11:15

'''


def maxProfit( prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if len(prices) == 0:
        return 0
    res = 0
    tempmin = prices[0]
    for i in prices[1:]:
        if i < tempmin:
            tempmin = i
        else:
            res = max(res, i - tempmin)
    return res


if __name__ == '__main__':
    pass

