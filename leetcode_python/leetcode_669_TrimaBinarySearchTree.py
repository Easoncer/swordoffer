# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_669_TrimaBinarySearchTree.py

@time: 2018/3/31 上午1:21

'''


def trimBST(self, root, L, R):
    """
    :type root: TreeNode
    :type L: int
    :type R: int
    :rtype: TreeNode
    """
    if not root:
        return None
    if root.val < L:
        return self.trimBST(root.right, L, R)
    if root.val > R:
        return self.trimBST(root.left, L, R)
    root.left = self.trimBST(root.left, L, R)
    root.right = self.trimBST(root.right, L, R)

    return root

if __name__ == '__main__':
    pass

