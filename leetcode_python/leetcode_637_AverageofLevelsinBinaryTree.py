# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode_637_AverageofLevelsinBinaryTree.py

@time: 2018/4/2 上午10:53

'''


def averageOfLevels( root):
    """
    :type root: TreeNode
    :rtype: List[float]
    """
    queue = [root]
    res = []
    while queue:
        count = len(queue)
        sumnode = 0
        for i in range(count):
            node = queue.pop(0)
            sumnode += node.val
            if node.right is not None:
                queue.append(node.right)
            if node.left is not None:
                queue.append(node.left)
        res.append(float(sumnode) / count)
    return  res

if __name__ == '__main__':
    pass

