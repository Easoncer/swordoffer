# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_513_FindBottomLeftTreeValue.py

@time: 2018/4/1 下午9:16

'''


def findBottomLeftValue( root):
    """
    :type root: TreeNode
    :rtype: int
    """
    queue = [root]
    for i in queue:
        queue.extend(filter(None, (i.right, i.left)))
    return i.val

if __name__ == '__main__':
    pass

