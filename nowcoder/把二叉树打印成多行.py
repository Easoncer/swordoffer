# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 把二叉树打印成多行.py

@time: 2018/6/9 下午9:54

'''


class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        Nodelist = []
        res = []

        if pRoot is None:
            return []
        Nodelist.append(pRoot)

        while Nodelist:
            templist = []
            n = len(Nodelist)
            for i in range(n):
                node = Nodelist.pop(0)
                templist.append(node.val)

                if node.left:
                    Nodelist.append(node.left)
                if node.right:
                    Nodelist.append(node.right)

            res.append(templist)
        return res

if __name__ == '__main__':
    pass

