# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 字符流中第一个不重复的字符.py

@time: 2018/5/30 下午2:44

'''
str=''
str_dic={}

def FirstAppearingOnce():
    if str_dic is {}:
        return "#"
    for i in str:
        if str_dic[i] == 1:
            return i
    return  "#"


# write code here
def Insert( char):
    global str
    global str_dic
    str += char
    if char in str_dic:
        str_dic[char] += 1
    else:
        str_dic[char] = 1

if __name__ == '__main__':
    pass

