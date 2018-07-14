# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 3.py

@time: 2018/7/12 上午10:59

'''
def duplicate(numbers):
    if len(numbers) == 0:
        return False

    length = len(numbers)

    for value in numbers:
        if value >= length:
            value -= length

        if numbers[value] >= length:
            return value
        else:
            numbers[value] += length


if __name__ == '__main__':
    print duplicate([2,3,1,0,0])

