//
// Created by 李先生 on 2018/9/3.
//

#include <iostream>
#include <vector>
using namespace std;

const int inf=999999;


void dijistra(vector<vector<int>> &e, int m, int n) {
    //初始化参数
    vector<int> visited(e.size(), 0);
    int last_visited = 0;
    int v0 = 0;
    visited[v0] = 1;

    vector <int>res = {n, inf};

    for(int i = 0; i < e.size()-1;i++)
    {
        for(int j = 0 ;j < e.size()-1; j++)
        {
            if (visited[j] == 0) //表示未访问
            {
                int dist = e[v0][j] + last_visited;
                if (dist < res[j]) res[j] = dist;
            }
            // 然后取出最小值

            int minindex = 0 ;
            while (visited[minindex] == 1) minindex++;
            for(int i = 0; i< e.size(); i++)
            {
                if (visited[i] == 0 && res[minindex] > res[i])
                {
                    minindex = i;
                }
            }

            last_visited = res[minindex];
            visited[minindex] = 1;
            v0 = minindex;
        }
    }
}

int main()
{
    vector<vector<int>> s_graph = {{inf,2,inf,inf,2,10},{inf,inf,inf,inf,inf,6},{inf,inf,inf,inf,inf,1},{inf,inf,inf,inf,inf,inf},{inf,inf,1,inf,inf,inf},{inf,inf,inf,inf,inf,inf}};
    int row = s_graph.size();
    int col = s_graph[0].size();
//    floyd(s_graph, row, col);

    for(int i=0; i < row;i++) {
        for (int j = 0; j < col; j++) {
            cout << s_graph[i][j] << endl;
        }
    }
    return 0;
}

