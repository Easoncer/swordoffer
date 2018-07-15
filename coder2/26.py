# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 26.py

@time: 2018/7/15 下午5:12

'''


def isSub(self, p1, p2):
    if p2 is None:
        return True
    if p1 is None:
        return False
    if p1.val != p2.val:
        return False
    return self.isSub(p1.left, p2.left) and self.isSub(p1.right, p2.right)


def HasSubtree(self, pRoot1, pRoot2):
    # write code here
    if pRoot2 is None or pRoot1 is None:
        return False
    flag = self.isSub(pRoot1, pRoot2)
    if not flag:
        flag = self.HasSubtree(pRoot1.left, pRoot2)
    if not flag:
        flag = self.HasSubtree(pRoot1.right, pRoot2)
    return flag

if __name__ == '__main__':
    pass

