# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_114_FlattenBinaryTreetoLinkedList.py

@time: 2018/7/26 上午10:56

'''

# Definition for a binary tree node.
class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def flatten( root, res):
    """
    :type root: TreeNode
    :rtype: void Do not return anything, modify root in-place instead.
    """
    if not root:
        return None
    res.append(root)
    flatten(root.left,res)
    flatten(root.right,res)
    return res

def flat(root):
    res = []
    res = flatten(root, res)
    if not res:
        return None

    for index in range(len(res)-1):
        res[index].left  = None
        node[index].right = node[index+1]


if __name__ == '__main__':
    tree = node(1, node(2, node(3), node(4)), node(5, node(6), node(7)))


