# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: treeNode.py

@time: 2018/7/26 上午11:01

'''

class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

if __name__ == '__main__':
    tree = node(5, node(3, node(2), node(4)), node(7, node(6), node(8, node(6))))


