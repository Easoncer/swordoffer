# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_102_BinaryTreeLevelOrderTraversal.py

@time: 2018/4/13 下午1:53

'''


def levelOrder( root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    if root is None:
        return []
    nodestack = [root]
    res = [[root.val]]

    while nodestack:
        num = len(nodestack)
        reslist = []
        for i in range(num):
            tempnode = nodestack.pop(0)
            if tempnode.left is not None:
                reslist.append(tempnode.left.val)
                nodestack.append(tempnode.left)
            if tempnode.right is not None:
                reslist.append(tempnode.right.val)
                nodestack.append(tempnode.right)
        if reslist:
            res.append(reslist)
    return res


if __name__ == '__main__':
    pass

