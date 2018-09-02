#include <iostream>
#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <queue>
#include <map>
using namespace std;

int main() {
    map<int, int> dic;
    dic[1] = 2;
    dic[2] = 3;

    map<int, int> ::iterator iter = dic.find(3);
    if(dic.count(3))
    {
        cout << "" ;
    }
    vector<int> nums = {9, 6, 2, 4, 7, 0, 1, 8, 3, 5};

    return 0;
}