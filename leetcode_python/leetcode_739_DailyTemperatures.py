# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_739_DailyTemperatures.py

@time: 2018/4/3 下午12:55

'''


def dailyTemperatures( temperatures):
    """
    :type temperatures: List[int]
    :rtype: List[int]
    """
    nums = len(temperatures)
    b = {}
    index = []
    for i in range(nums):
        while len(index) != 0 and temperatures[index[-1]] < temperatures[i]:
            b[index.pop()] = i

        index.append(i)
    res = []
    for i in range(nums):
        if i in b:
            res.append(b[i] - i)
        else:
            res.append(0)
    return res

if __name__ == '__main__':
    pass

