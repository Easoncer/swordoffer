# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 数组中只出现一次的数字.py

@time: 2018/5/28 上午11:00

'''


# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        number = reduce(lambda x, y: x ^ y, array)
        number = bin(number)[2:]

        flag = 1 << (len(number) - 1)
        one_div, two_div = [], []
        for i in array:
            if i & flag:
                one_div.append(i)
            else:
                two_div.append(i)
        return [reduce(lambda x, y: x ^ y, one_div), reduce(lambda x, y: x ^ y, two_div)]


if __name__ == '__main__':
    pass

