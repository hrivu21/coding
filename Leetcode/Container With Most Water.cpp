#include<bits/stdc++.h>
#include<iostream>
#include<string>
#include<vector>
#include<list>
#include<set>
#include<map>
#include<math.h>

using namespace std;


template <typename T>   // use of generic
string str_vector(vector<T> v){
    string s = "[ ";
    for(auto i: v){
        s += to_string(i) + " ";
    }
    return s+"]";
}


class Solution {
public:
    int findMaxArea(vector<int>&  height, int i1, int i2, int maxCap){
        if (i1 == i2)
            return maxCap;

        maxCap = max(maxCap, min(height[i1], height[i2])*(i2-i1));

        if (height[i1] < height[i2])
            return findMaxArea(height, i1+1, i2, maxCap);
        else 
            return findMaxArea(height, i1, i2-1, maxCap);
    }

    int maxArea(vector<int>& height) {
        int maxCap = 0;
        return findMaxArea(height, 0, height.size()-1, maxCap);
    }
};

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 

    Solution obj;
    vector<int> height{1,8,6,2,5,4,8,3,7};

    cout << obj.maxArea(height);

    return 0;
}