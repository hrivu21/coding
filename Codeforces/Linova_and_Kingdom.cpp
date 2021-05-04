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



struct Node{
    int num;
    long long depth;
    long long descndnts;
    bool visited;
};


string str_node(Node n){
    return to_string(n.num) + " " + to_string(n.depth) + 
                              " " + to_string(n.descndnts)+ " " + to_string(n.visited) ;
}


vector<Node> Nodes;
map<int, vector<int>> adj;      // contains the indices of the Node structs

int n;      // #cities;
int k;      // #Industrial cities;



long long dfs(int node_index, long long d){
    Node& node = Nodes[node_index];
    node.visited = true;
    node.depth = d;

    long long cnt_desc = 0;

    for(int child_index: adj[node_index]){
        Node& child = Nodes[child_index];

        if(child.visited == false){
            cnt_desc += 1 + dfs(child_index, d+1);
        }
    }

    node.descndnts = cnt_desc;
    return cnt_desc;
}



bool compareNodes(Node n1, Node n2){
    // if(n1.depth > n2.depth){
    //     return true;
    // }
    // else if(n1.depth == n2.depth){
    //     return (n1.descndnts <= n2.descndnts);
    // }
    // else{
    //     return false;
    // }

    return (n1.depth - n1.descndnts) > (n2.depth - n2.descndnts);
}



int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 

    cin >> n >> k;

    for(int i=1; i<=n; i++){
        Nodes.push_back({i, 0, 0, false});
    }

    int u, v;
    for(int i=0; i<n-1; i++){
        cin >> u >> v;
        u -= 1;
        v -= 1;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    int x = dfs(0, 0);

    // cout << "Assert: " << (x == (n-1)) << endl;

    // for(int i=0; i<Nodes.size(); i++){
    //     cout << str_node(Nodes[i]) << endl;
    // }

    sort(Nodes.begin(), Nodes.end(), compareNodes);

    // cout << "-----------After sorting------------" << endl;
    // for(int i=0; i<Nodes.size(); i++){
    //     cout << str_node(Nodes[i]) << endl;
    // }

    long long total_happiness = 0;

    for(int i=0; i<k; i++){
        total_happiness += (Nodes[i].depth - Nodes[i].descndnts);
    }

    cout << total_happiness << endl;

    return 0;

}