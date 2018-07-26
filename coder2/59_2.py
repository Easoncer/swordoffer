# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 59_2.py

@time: 2018/7/26 下午5:42

'''
# 构造两个队列，然后一个队列存储值，还有一个队列存储当前对垒的最大值


class MaxFront:
    def __init__(self):
        self.front = []
        self.maxfront = []
    def adddata(self,data):

        if not self.maxfront or self.maxfront[-1] >= data:
            self.maxfront.append(data)
        else:
            while self.maxfront and  self.maxfront[-1] < data:
                self.maxfront.pop()
            self.maxfront.append(data)
        self.front.append(data)

    def popdata(self):

        temp = self.front.pop(0)
        if temp == self.maxfront[0]:
            self.maxfront.pop(0)
        return temp

    def theFrontMax(self):
        return self.maxfront[0]

if __name__ == '__main__':
    front = MaxFront()
    front.adddata(1)
    front.adddata(3)
    front.adddata(4)
    front.adddata(3)
    print front.front, front.maxfront

    print front.theFrontMax()
    front.popdata()
    front.popdata()
    front.popdata()
    print front.front, front.maxfront

    print front.theFrontMax()



