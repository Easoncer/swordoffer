# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 53_2.py

@time: 2018/7/24 下午2:35

'''
def getMissingNumber(temp):

    left, right = 0, len(temp) - 1

    while left <= right:
        mid = (left+right)/2
        if temp[mid] == mid :
            left = mid+1
        else:
            if mid == 0 or temp[mid-1] == mid - 1:
                return mid
            right = mid - 1
    if left == len(temp):
        return left
    return -1

if __name__ == '__main__':
    print getMissingNumber([0,1,2,3,4])

