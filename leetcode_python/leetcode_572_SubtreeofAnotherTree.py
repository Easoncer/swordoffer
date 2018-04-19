# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_572_SubtreeofAnotherTree.py

@time: 2018/4/19 下午5:30

'''


def isSubtree(self, s, t):
    """
    :type s: TreeNode
    :type t: TreeNode
    :rtype: bool
    """

    def isSame(snode, tnode):
        if not snode and not tnode:
            return True
        if snode and tnode and snode.val == tnode.val:
            return isSame(snode.left, tnode.left) and isSame(snode.right, tnode.right)
        return False

    if s is None:
        return False
    return isSame(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


if __name__ == '__main__':
    pass

