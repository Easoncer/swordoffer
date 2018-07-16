# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 40.py

@time: 2018/7/16 下午3:37

'''
def partition(temp, left, right):
    key = temp[right]
    i, j = left, left
    for j in range(left, right ):
        if temp[j] < key:
            temp[i], temp[j] = temp[j],temp[i]
            i += 1
        j += 1
    temp[i], temp[j] = temp[j], temp[i]

    return i

def getLeastNumber(templist, left, right, k):
    i = partition(templist, left, right)

    if i > k:
        getLeastNumber(templist, 0, i-1, k)
    if i < k:
        getLeastNumber(templist, i, right, k-i)
    return templist[:k]

if __name__ == '__main__':
    print getLeastNumber([4,5,1,6,2,7,3,8], 0, 7, 5)

