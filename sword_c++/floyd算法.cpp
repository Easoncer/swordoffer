//
// Created by 李先生 on 2018/9/3.
//

#include <iostream>
#include <vector>
using namespace std;

const int inf=999999;

void floyd(vector<vector<int>> &e, int m, int n) {
    int i, j, k;
    for (i = 0; i < n; i ++) {
        for (j = 0; j < m; j++) {
            for (k = 0; k < n; k++) {
                if ( e[i][j] > e[i][k] + e[k][j])
                    e[i][j] = e[i][k] + e[k][j];
            }
        }
    }
}

int main()
{
    vector<vector<int>> s_graph = {{inf,2,inf,inf,2,10},{inf,inf,inf,inf,inf,6},{inf,inf,inf,inf,inf,1},{inf,inf,inf,inf,inf,inf},{inf,inf,1,inf,inf,inf},{inf,inf,inf,inf,inf,inf}};
    int row = s_graph.size();
    int col = s_graph[0].size();
    floyd(s_graph, row, col);

    for(int i=0; i < row;i++) {
        for (int j = 0; j < col; j++) {
            cout << s_graph[i][j] << endl;
        }
    }
    return 0;
}


