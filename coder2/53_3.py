# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 53_3.py

@time: 2018/7/24 下午3:04

'''
def getNumber(temp):
    left, right = 0, len(temp)
    while left <= right:
        mid = (left + right) /2
        if temp[mid] == mid:
            return mid
        if temp[mid] > mid:
            right = mid - 1
        if temp[mid] < mid:
            left = mid + 1

if __name__ == '__main__':
    print getNumber([-3,-1,1,3,5])

