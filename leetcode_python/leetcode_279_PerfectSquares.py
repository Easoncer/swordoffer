# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_279_PerfectSquares.py

@time: 2018/7/26 上午12:45

'''
# 这个博客写的不错，可以参考

# https://blog.csdn.net/happyaaaaaaaaaaa/article/details/51584790


# 复杂度比较高，但是应该是可以过的。。。但是我Time Limit Exceeded
import  math
def numSquares(n):
    temp = [0 for i in range(n+1)]
    index = 1
    while index*index <= n:
        temp[index*index] = 1
        index += 1

    for i in range(2,n+1):
        if temp[i] == 1:
            continue
        res = 100
        for j in range(1, i):
            res = min(res, temp[j]+temp[i-j])
        temp[i] = res
    print temp
    return temp[n]
#13  -> [0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 3, 2]
# 方法还是得改进


## 虽然方法和前面方法不一样， 但是原理基本相同
import  math
def numSquaresSecond(n):
    temp = [0 for i in range(n+1)]
    index = 1
    while index*index <= n:
        temp[index*index] = 1
        index += 1

    base = 0
    for i in range(1,n+1):
        if temp[i] == 1:
            base += 1
            continue
        res = 100
        for j in range(1,base+1):
            res = min(1 + temp[i - j*j],res)
        temp[i] = res
    print temp
    return temp[n]


if __name__ == '__main__':
    print numSquaresSecond(13)

