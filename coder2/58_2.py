# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 58_2.py

@time: 2018/7/26 下午4:32

'''
def leftRotateString(str, key):
    return str[key:] + str[:key]

if __name__ == '__main__':
    print leftRotateString('abcdefg',2)

