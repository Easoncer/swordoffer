# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 左旋转字符串.py

@time: 2018/5/28 下午2:37

'''
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        return s[n:] + s[:n]


if __name__ == '__main__':
    pass

