//
// Created by 李先生 on 2018/9/5.
//
#include <iostream>
#include <vector>
using namespace std;



class Solution {
public:
    struct  node
    {
        int x;
        int y;
        node(int x_, int y_):
            x(x_), y(y_){};
    };

    bool right(int x, int y, int threshold)
    {
        int res = 0;
        while (x)
        {
            res += x%10;
            x = x/10;
        }
        while(y)
        {
            res += y%10;
            y = y/10;
        }
        return  res <= threshold;
    }


    int movingCount(int threshold, int rows, int cols)
    {
        vector<node> node_v;
        if (rows < 0 || cols <0 || threshold < 0)
            return 0;
        vector<bool > mark(rows*cols, false);
        node_v.push_back(node(0,0));
        int res = 0;
        while (!node_v.empty())
        {
            node Node = node_v.front();
            node_v.erase(node_v.begin());
            res += 1;

            if (Node.x + 1 < cols && right(Node.x+1, Node.y, threshold) && !mark[Node.x + 1 + Node.y * cols])
            {
                mark[Node.x + 1 + Node.y * cols] = true;
                node_v.push_back(node(Node.x+1, Node.y));
            }
            if (Node.y + 1 < rows && right(Node.x, Node.y + 1, threshold) && !mark[Node.x + (Node.y + 1) * cols])
            {
                mark[Node.x + (Node.y+1) * cols] = true;
                node_v.push_back(node(Node.x, Node.y+1));
            }
        }
        return res;
    }
};

int main()
{
    Solution s;
    cout << s.right(35,37,18) <<endl;
    return 0;
}