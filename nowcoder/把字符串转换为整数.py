# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 把字符串转换为整数.py

@time: 2018/5/28 下午10:15

'''
# 剑指offer 127页的题目
# 这个题目的要求比较简单

def StrToInt( s):
    # write code here
    if len(s) == 0:
        return 0
    n = len(s)
    flag = 1
    if s[0] == '-':
        flag = -1
        start = 1
    elif s[0] == '+':
        start = 1
    else:
        start = 0
    if start == n:
        return 0

    for i in range(start, n):
        if not ('0' <= s[i] and s[i] <= '9'):
            return 0
    if s[0] == '+':
        return int(s[1:])
    else:
        return int(s)


if __name__ == '__main__':
    pass

