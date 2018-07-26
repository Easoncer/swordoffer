# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 58.py

@time: 2018/7/26 下午4:28

'''

def reverseString(stringList):
    temp = stringList.split(' ')
    temp.reverse()
    return ' '.join(temp)

if __name__ == '__main__':
    print reverseString('I am a student.')

