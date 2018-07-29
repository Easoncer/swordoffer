# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_105_ConstructBinaryTreefromPreorderandInorderTraversal.py

@time: 2018/7/28 下午5:27

'''
class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def buildTree( preorder, inorder):
    """
    :type preorder: List[int]
    :type inorder: List[int]
    :rtype: TreeNode
    """
    if not preorder or not inorder:
        return None

    nodeval = preorder[0]
    #print nodeval
    #print preorder[1:inorder.index(nodeval) + 1], inorder[:inorder.index(nodeval)]
    root = node(nodeval)
    root.left = buildTree(preorder[1:inorder.index(nodeval) + 1], inorder[:inorder.index(nodeval)])
    #print "here"
    #print preorder[inorder.index(nodeval)+1:], inorder[inorder.index(nodeval) + 1:]
    root.right = buildTree(preorder[inorder.index(nodeval)+1:], inorder[inorder.index(nodeval) + 1:])
    return root

if __name__ == '__main__':
    #tree = node(5, node(3, node(2), node(4)), node(7, node(6), node(8, node(6))))
    # preorder [3, 9, 20, 15, 7]
    # inorder  [9, 3, 15, 20, 7]
    print buildTree([3, 9, 20, 15, 7],[9, 3, 15, 20, 7])

