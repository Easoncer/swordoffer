# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 和为S的连续正数序列.py

@time: 2018/5/28 上午11:23

'''


def FindContinuousSequence( tsum):
    # write code here
    res = []
    p, q = 1, 1
    slide_sum = 1
    while p <= tsum / 2:
        if slide_sum < tsum:
            q += 1
            slide_sum += q
        elif slide_sum > tsum:
            slide_sum -= p
            p += 1
        else:
            res.append(range(p, q +1))
            slide_sum -= p
            p += 1
    return res
if __name__ == '__main__':
    print FindContinuousSequence(100)

