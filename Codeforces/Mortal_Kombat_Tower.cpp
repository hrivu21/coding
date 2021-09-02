// AC

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



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 

    int t, n;
    vector<bool> a(200002);

    cin >> t;

    while(t--){
        cin >> n;
        int i, x;
        for(i=0; i<n; i++){
            cin >> x;
            a[i] = x;
        }

        int skip = 0;
        skip += a[0];
        i = 1;

        while(i < n){
            if(!a[i]){
                i += 1;
                continue;
            }

            int c = 0;
            while(i<n && a[i]){
                c++;
                i += 1;
            }

            // cout << "c " << c << endl;
            skip += floor(c/3);
        }
        // cout << "skip = " << skip << endl;
        cout << skip << endl;
    }    

    return 0;
}
