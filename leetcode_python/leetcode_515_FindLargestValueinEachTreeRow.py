# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_515_FindLargestValueinEachTreeRow.py

@time: 2018/4/2 下午1:21

'''


def largestValues( root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    queue = [root]
    res = []
    while queue:
        res.append(max(map(lambda _: _.val, queue)))
        num = len(queue)
        for i in range(num):
            node = queue.pop(0)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return res


if __name__ == '__main__':
    pass

