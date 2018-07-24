# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 53.py

@time: 2018/7/24 下午12:15

'''

def getLeftNumber(sortedlist, key):
    left, right = 0,len(sortedlist)-1

    while left  <= right:
        mid = (left+right)/2
        if key > sortedlist[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return left

def getRightNumber(sortedlist, key):
    left, right = 0,len(sortedlist)-1

    while left  <= right:
        mid = (left+right)/2
        if key < sortedlist[mid]:
            right = mid -1
        else:
            left = mid+1
    return right


if __name__ == '__main__':
    #left = getLeftNumber([1,2,3,3,3,3,4,5],3)
    #right = getRightNumber([1, 2, 3, 3, 3, 3, 4, 5], 3)
    left = getLeftNumber([1,2,2,5],2)
    right = getRightNumber([1, 2,2, 5], 2)
    print left, right
    print right - left + 1

