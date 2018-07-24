# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 55.py

@time: 2018/7/24 下午3:31

'''
class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def deepthTree(root):
    if not root:
        return  0
    return  max(deepthTree(root.left), deepthTree(root.right) )+ 1

if __name__ == '__main__':
    tree = node(5, node(3, node(2), node(4)), node(7, node(6), node(8, node(6))))
    print deepthTree(tree)

