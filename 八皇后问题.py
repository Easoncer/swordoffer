# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 八皇后问题.py

@time: 2018/8/2 下午10:14

'''

# 类似于排列的一种

def Queen(mark, res, step):

    if len(res) == 8:
        print res
        return

    for i in range(8):
        if mark[i] == 0:
            mark[i] = 1
            res.append(i)
            Queen(mark, res, step + 1)
            res.pop()
            mark[i] = 0

if __name__ == '__main__':
    mark = [0 for i in range(8)]
    res = []
    Queen(mark, res, 0)

