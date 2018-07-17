
# encoding: utf-8

'''

@author: liangchi

@contact: bnu_llc@163.com

@software: pycharm

@file: 46.py

@time: 2018/7/17 下午2:33

'''

def getTranslation(n):
    listn = str(n)

    if len(listn) == 1:
        return 1
    res = [1,1]
    for i in range(1,len(listn)):
        print listn[i]
        if listn[i-1:i+1] >= "10" and listn[i-1:i+1] <= "25":
            flag = 1
        else:
            flag = 0
        res.append(res[i]+flag*res[i-1])
    return res

if __name__ == '__main__':
    print getTranslation(12258)

