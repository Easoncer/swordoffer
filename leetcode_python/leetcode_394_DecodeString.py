# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_394_DecodeString.py

@time: 2018/4/16 下午10:12

'''
def decodeString(s):
    stacknum = []
    stackstr = []
    i = 0

    while i < len(s):

        if s[i].isdigit():
            j = i
            while s[j+1].isdigit():
                j += 1
            stacknum.append(int(s[i :j+1]))
            i = j+1

        elif s[i] == '[':
            stackstr.append(s[i])
            i += 1

        elif s[i] == ']':
            str = ''
            num = stacknum.pop()
            while stackstr[-1] != '[':
                str = stackstr.pop() + str
            stackstr.pop()
            stackstr.append(num*str)
            i += 1
        else:
            j = i
            while j+1< len(s) and s[j+1].isalpha():
                j += 1
            stackstr.append(s[i: j+1])
            i = j+1

    return ''.join(stackstr)

if __name__ == '__main__':
    print decodeString('2[abc]3[cd]ef')

