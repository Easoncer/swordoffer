# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_344_ReverseString.py

@time: 2018/3/30 下午10:17

'''
def reverseString( s):

        s =list(s)
        s.reverse()
        return ''.join(s)

#       return s[::-1]
if __name__ == '__main__':
    print reverseString('abc')

