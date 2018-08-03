# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 背包问题.py

@time: 2018/8/3 上午10:36

'''

def bagProblem(s, weights,mark, res,step):
    # s : sum bags weight
    # weights : objects weights
    if s == 0:
        print res
        return True
    if s < 0:
        return False


    for i in range(len(weights)):
        if mark[i] == 0 and step <= i:
            mark[i] = 1
            #print step, i
            res.append(weights[i])
            bagProblem(s-weights[i], weights, mark,res, i)
            res.pop()
            mark[i] = 0

if __name__ == '__main__':
    weights = [2,2,6,5,4]
    s = 10
    mark = [0 for i in range(len(weights))]
    res = []
    bagProblem(s, weights,mark, res, 0)


