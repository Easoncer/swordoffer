# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 9.py

@time: 2018/7/12 下午7:28

'''


def __init__(self):
    self.stackA = []
    self.stackB = []


def push(self, node):
    # write code here
    self.stackA.append(node)


def pop(self):
    # return xx
    if not self.stackA:
        return None
    while self.stackA:
        self.stackB.append(self.stackA.pop())
    temp = self.stackB.pop()

    while self.stackB:
        self.stackA.append(self.stackB.pop())
    return temp

if __name__ == '__main__':
    a = [1]
    if a:
        print "true"
