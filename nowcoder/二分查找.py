# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 二分查找.py

@time: 2018/6/3 下午12:03

'''

def twoSort(numlist, key):
    left = 0
    right = len(numlist) -1
    while left <= right:
        mid = (left+right)/2
        if numlist[mid] < key:
            left = mid+1
        elif numlist[mid] > key:
            right = mid-1
        else :
            return mid
    return  "not found"

if __name__ == '__main__':
    print  twoSort([11], key = 10)

