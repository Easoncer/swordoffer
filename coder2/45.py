# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 45.py

@time: 2018/7/17 下午2:25

'''
def PrintMinNumber( numbers):
    def decide(x, y):
        tempx = int(str(x) + str(y))
        tempy = int(str(y) + str(x))
        return tempx - tempy

    temp = sorted(numbers, cmp=decide, reverse=False)
    return  ''.join(map(lambda x:str(x), temp))

if __name__ == '__main__':
    pass

