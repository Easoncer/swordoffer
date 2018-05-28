# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 翻转单词顺序列.py

@time: 2018/5/28 下午2:40

'''


def ReverseSentence(s):

    #return ' '.join(s.split()[::-1])
    return ' '.join(s.split(' ')[::-1])


if __name__ == '__main__':
    print ReverseSentence("student. a am I")

