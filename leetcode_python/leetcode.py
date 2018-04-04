# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: leetcode.py

@time: 2018/4/4 下午8:48

'''

s= 0
def convertBST( root):
    """
    :type root: TreeNode
    :rtype: TreeNode
    """
    # first of all , we compute the inorder result

    temp = []

    def visit1(root):
        if root:
            visit1(root.left)
            temp.append(root.val)
            visit1(root.right)

    visit1(root)

    global  s

    def visit2(root):
        if root:
            visit2(root.right)
            s += temp.pop()
            root.val = s
            visit2(root.left)

    visit2(root)
    return root

if __name__ == '__main__':
    pass

