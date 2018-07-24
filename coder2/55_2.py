# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 55_2.py

@time: 2018/7/24 下午3:34

'''

class node(object):
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def IsBalanced_Solution( pRoot):
    bool_flag, depth = IsBalanced(pRoot)
    return bool_flag

def IsBalanced(pRoot):
    if not pRoot:
        return True, 0
    bool_left, left_depth = IsBalanced(pRoot.left)
    bool_right, right_depth = IsBalanced(pRoot.right)

    if bool_left and bool_right:
        diff = left_depth - right_depth
        if -1 <= diff <= 1:
            depth = left_depth
            if diff < 0:
                depth = right_depth
            return True, depth + 1

    return False, 0

if __name__ == '__main__':
    pass

