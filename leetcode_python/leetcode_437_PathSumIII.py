# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_437_PathSumIII.py

@time: 2018/4/19 下午5:53

'''


def __init__(self):
    self.count = 0


def pathSum(self, root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: int
    """

    def findsumpath(node, tempsum, sum):
        if tempsum == sum:
            self.count += 1
            return

        if node:
            findsumpath(node.left, tempsum + node.val, sum)
            findsumpath(node.right, tempsum + node.val, sum)

    if root is None:
        return 0

    tempsum = 0

    findsumpath(root, tempsum, sum)
    self.pathSum(root.left, sum)
    self.pathSum(root.right, sum)
    return self.count / 2

if __name__ == '__main__':
    pass

