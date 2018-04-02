# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_104_MaximumDepthofBinaryTree.py

@time: 2018/4/2 下午3:18

'''


def maxDepth( root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    return max(maxDepth(root.right) + 1, maxDepth(root.left) + 1)


if __name__ == '__main__':
    pass

