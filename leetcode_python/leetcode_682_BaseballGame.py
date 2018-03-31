# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_682_BaseballGame.py

@time: 2018/3/31 下午4:12

'''


def calPoints( ops):
    """
    :type ops: List[str]
    :rtype: int
    """
    res = 0
    stacklist= []
    for i in ops:
        if i == 'C':
            num = stacklist.pop()
            res -= num
        elif i == 'D':
            temp = 2*stacklist[-1]
            stacklist.append(temp)
            res += temp
        elif i == '+':
            print stacklist
            temp = stacklist[-1]+stacklist[-2]
            res += temp
            stacklist.append(temp)
        else:
            stacklist.append(int(i))
            res +=int(i)
    return res


if __name__ == '__main__':
    print calPoints(["5","2","C","D","+"])

