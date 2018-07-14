# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 5.py

@time: 2018/7/12 下午3:55

'''
def replaceBlank(str):
    if len(str) == 0:
        return str

    count = 0

    for i in str:
        if i == ' ':
            count += 1
    i = len(str) - 1

    res = ''

    while i >= 0:

        if str[i] == ' ':
            res = '%20' + res
        else:
            res =  str[i] + res
        i -= 1

    return res


if __name__ == '__main__':
    print replaceBlank('we are happy')

