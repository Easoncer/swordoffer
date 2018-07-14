# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: two_divide.py

@time: 2018/7/12 下午2:24

'''
def two_devide(numlist, key):

    if len(numlist)==0:
        return 0

    left, right = 0, len(numlist)-1

    while left <= right:
        mid  = (left+right) /2
        if numlist[mid] < key:
            left = mid + 1
        elif numlist[mid] >key:
            right = mid - 1
        else:
            return mid
    return 0

if __name__ == '__main__':
    print two_devide([1,1,2,3,4,5,6,6.5,7],7)

