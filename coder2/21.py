# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 21.py

@time: 2018/7/15 上午10:54

'''
def change(temp):
    if not temp:
        return []
    i, j = 0, 0
    while j < len(temp):
        if temp[j] % 2:
            temp[i], temp[j] = temp[j], temp[i]
            i += 1
        j += 1
    return temp

if __name__ == '__main__':
    print change([1,2,3,4,5,6,7,8])

