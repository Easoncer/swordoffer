# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_500_KeyboardRow.py

@time: 2018/3/31 上午12:57

'''

def findWords( words ):
    row1 = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']
    row2 = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
    row3 = ['z', 'x', 'c', 'v', 'b', 'n', 'm']
    res = []
    for i in words:
        # temp = i.lower()
        temp = i.lower()
        print temp

        if temp[0] in row1:
            classlabel = row1
        elif temp[0] in row2:
            classlabel = row2
        else:
            classlabel = row3
        print classlabel
        j = 0
        for j in range(1, len(i)):
            if temp[j] not in classlabel:
                break
        if (j == len(i) - 1) and (temp[-1] in classlabel):
            res.append(i)
    return res

if __name__ == '__main__':
    print findWords(["zZxcvbnm"])

