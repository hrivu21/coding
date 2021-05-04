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
    return s+" ] ";
}



class Graph{

    public :
        int nVertices;
        int nEdges;
        map<int, vector<int>> adj;
        vector<bool> visited;

        Graph(int v, int e){
            nVertices = v;
            nEdges = e;
            visited.assign(nVertices+1, false);
        }



    void addEdge(int s, int d){
        adj[s].push_back(d);
        adj[d].push_back(s);
    }



    bool is_cycle(int curr_node){

        visited[curr_node] = true;
        // cout << "Visited: " << curr_node << endl;

        bool cycle_flag = true;

        if(adj[curr_node].size() != 2) cycle_flag = false;

        for(int child: adj[curr_node]){
            if(visited[child] == false){
                cycle_flag = is_cycle(child) && cycle_flag;     // take care bcoz of short-circuit nature of logical and
            }
        }
        return cycle_flag;
        // visited[curr_node] = false;
    }



    int count_cycles(){
        int trees = 0;
        int cycles = 0;

        for(int i = 1; i < visited.size(); i++){
            if(visited[i] == false){
                trees += 1;

                if(is_cycle(i)) cycles += 1 ;

                // cout << "Tree start : " << i << endl;
                // cout << str_vector<bool>(visited) << endl;
            }
        }

        // cout << "# trees= " << trees << endl;
        return cycles;
    }
};




int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); 
    
    int vv, ee;
    cin >> vv >> ee;

    Graph graph(vv, ee);

    int x, y;
    for(int i=0; i<ee; i++){
        cin >> x >> y;
        graph.addEdge(x, y);
    }

    // for(int i=1; i<=graph.nVertices; i++){
    //     cout << i << " : " << str_vector<int>(graph.adj[i]) << endl;
    // }

    int cycles = graph.count_cycles();

    cout << cycles << "\n";

    // for(int i=0; i<=graph.nVertices; i++){
    //     cout << graph.visited[i] << " ";
    // }
    return 0;
}

