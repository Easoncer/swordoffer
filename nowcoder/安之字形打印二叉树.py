# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 安之字形打印二叉树.py

@time: 2018/5/30 下午8:16

'''


def Print( pRoot):
    # write code here
    reslist = []
    Nodelist = []
    if pRoot is None:
        return reslist
    Nodelist.append(pRoot)
    flag = 1

    while Nodelist:
        temp = []
        num = len(Nodelist)
        for i in range(num):
            Node = Nodelist.pop(0)
            temp.append(Node.val)

            if Node.left is not None:
                Nodelist.append(Node.left)
            if Node.right is not None:
                Nodelist.append(Node.right)
        flag *= -1
        if flag == 1: temp.reverse()
        reslist.append(temp)

    return reslist


if __name__ == '__main__':
    a = [1,2,3,4]
    for i in range(len(a)):
        print i
