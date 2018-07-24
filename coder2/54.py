# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 54.py

@time: 2018/7/24 下午3:17

'''

class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def inorderTree(root, res):
    if not root :
        return None
    inorderTree(root.left,res)
    res.append(root.data)
    inorderTree(root.right,res)
    return res

def kthMax(root,k):

    res = inorderTree(root, [])
    if len(res) < k:
        return None
    else:
        return res[k-1]


if __name__ == '__main__':
    tree = node(5, node(3, node(2), node(4)), node(7, node(6), node(8)))
    #print inorderTree(tree, [])
    print kthMax(tree, 3)

