#include <bits/stdc++.h>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <math.h>

using namespace std;

template <typename T> // use of generic
string str_vector(vector<T> v)
{
    string s = "[ ";
    for (auto i : v)
    {
        s += to_string(i) + " ";
    }
    return s + "]";
}

class Solution
{
public:
    int jump(vector<int> &nums){
        int jmp_cnt = 0;
        set<int> visited;

        vector<int> queue{0};
        visited.insert(0);

        while queue.size(){
            int index = queue.pop_back();
            for (int i = index; i <= index + nums[index]; i++){
                if find (queue[i]) != queue.end() {
                    queue.push_back(i);
                }
            }
        }
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    return 0;
}
