# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 39.py

@time: 2018/7/16 下午4:12

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

def Morethanhalf(templist, left, right):
    half = (len(templist)+1)/2
    index = partition(templist, left, right)
    print index
    print templist
    if index < half:
        Morethanhalf(templist, index+1, right)
    if index > half:
        Morethanhalf(templist, left, index-1)
    return templist[half]
    # if left < right:
    #     i = partition(templist, left, right)
    #     Morethanhalf(templist, left, i-1)
    #     Morethanhalf(templist, i+1, right)
    #
    # return templist
if __name__ == '__main__':
    print Morethanhalf([1,1,1,1,1,2,3,4], 0, 7)

