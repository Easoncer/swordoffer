# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 和为S的两个数字.py

@time: 2018/5/28 下午2:29

'''
# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        p, q = 0, len(array)-1
        temp = array[p] + array[q]
        while p <= q:
            if temp < tsum:
                p += 1
                temp = array[p]+array[q]
            elif temp > tsum:
                q -= 1
                temp = array[p]+array[q]
            else:
                return [array[p],array[q]]
        return []


if __name__ == '__main__':
    pass

