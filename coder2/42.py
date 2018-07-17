# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 42.py

@time: 2018/7/16 下午9:21

'''
def continusArr(temp_list):
    if not temp_list:
        return 0
    res = temp_list[0]
    temp = res
    for i in temp_list[1:]:
        temp += i
        if temp  < 0:
            temp = 0

        if res < temp:
            res = temp
    return res

if __name__ == '__main__':
    print continusArr([1,-2,3,10,-4,7,2,-5])

