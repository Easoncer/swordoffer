# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_101_SymmetricTree.py

@time: 2018/4/19 下午1:37

'''


def isSymmetric( root):
    """
    :type root: TreeNode
    :rtype: bool
    """

    def mirror(left, right):
        if not left and not right:
            return True
        if left and right and left.val == right.val:
            return mirror(left.right, right.left) and mirror(left.left, right.right)
        return False

    if root is None:
        return True
    if root.left is None and root.right is None:
        return True
    if root.left and root.right and root.left.val == root.right.val:
        return mirror(root.left, root.right)
    return False

if __name__ == '__main__':
    pass

