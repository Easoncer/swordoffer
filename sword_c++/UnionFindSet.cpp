//
// Created by 李先生 on 2018/9/3.
//
#include <iostream>
#include <vector>
#include <map>
using namespace std;

map<char, int> rootdict;   //key: root value: 结点值的数目
map<char, char> parent; //定义某个结点的父结点

void Make_Set(vector<vector<char>> relation)
{
    for (int i = 0; i< relation.size(); i++)
    {
        rootdict[relation[i][0]] = 1;
        rootdict[relation[i][1]] = 1;

        parent[relation[i][0]] = relation[i][0];
        parent[relation[i][1]] = relation[i][1];
    }
}

//返回根节点
char findroot(char x)
{
    map<char, int>::iterator iter;
    iter = rootdict.find(x);
//    发现存在对应key值
    if (iter != rootdict.end()) {
        return parent[x];
    } else {
        return findroot(parent[x]);
    }
}

void combine(char x, char y)
{
    char rootx = findroot(x);
    char rooty = findroot(y);

    int depx = rootdict[rootx];
    int depy = rootdict[rooty];

    // 按照深度来进行合并
    // 如果第一个树的深度比第二个深度大，将x 并到y树上
    if (depx >= depy)
    {
        parent[rooty] = rootx;
        rootdict.erase(rooty);
        rootdict[rootx] = depx + depy;
    } else{
        parent[rootx] = rooty;
        rootdict.erase(rootx);
        rootdict[rooty] = depx + depy;
    }
}

void createTree(vector<vector<char>> relation)
{
    for(int i =0 ; i < relation.size(); i++)
    {
//        判断根节点是不是一样？
        if (findroot(relation[i][0]) != findroot(relation[i][1]))
        {
            combine(relation[i][0], relation[i][1]);
        }
    }
}

int main()
{
    vector<vector<char>> relation = {{'a','b'},{'a','c'},{'a','d'},{'e','f'},{'f','g'}};
    Make_Set(relation);
    createTree(relation);

//    map<char, int>::iterator iter;
//////    for( iter = rootdict.begin(); iter != rootdict.end() ; iter ++ )
//////    {
//////        cout << findroot(iter->first) <<endl;
//////        cout << findroot(iter->second) <<endl;
//////    }

    for(int i =0 ; i < relation.size(); i++)
    {
        cout << findroot(relation[i][0]) <<endl;
        cout << findroot(relation[i][1]) <<endl;
    }
    return 0;
}