# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 56.py

@time: 2018/7/25 下午10:26

'''
def findSecondTime(temp):
    res = reduce(lambda x,y: x^y, temp)

    flag = 1

    while flag&res == 0:
        flag = flag<<1

    temp1, temp2 = [], []
    for i in temp:
        if i ^ flag:
            temp1.append(i)
        else:
            temp2.append(i)
    print temp2, temp1
    return [reduce(lambda x,y :x^y, temp1),reduce(lambda x,y :x^y, temp2)]

if __name__ == '__main__':
    print findSecondTime([1,2,3,2,3,4])

