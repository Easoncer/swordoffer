# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 11.py

@time: 2018/7/12 下午7:59

'''
def findmin(temp):
    left, right = 0, len(temp) - 1

    while left <= right:
        if right - left  == 1:
            return temp[right]

        mid = (left + right)/2

        if temp[mid] < temp[left]:
            right = mid

        if temp[mid] > temp[right]:
            left = mid

        if temp[mid] == temp[left] and temp[mid] == temp[right]:
            return min(temp)

if __name__ == '__main__':
    print findmin([1,1,1,0,1,1])

