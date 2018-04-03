# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_226_InvertBinaryTree.py

@time: 2018/4/3 下午12:52

'''


def invertTree( root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    if root is None:
        return None
    node = root.left
    root.left = invertTree(root.right)

    root.right = invertTree(node)
    return root

if __name__ == '__main__':
    pass

