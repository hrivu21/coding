#include <bits/stdc++.h>
#include <iostream>
#include <vector>
using namespace std;

class Tree{

	public:
		int n;		// no. of nodes
		int m;
		vector<int> a;
		map<int, list<int>> adj;	


	public:
		Tree(int nn, int mm){
			n = nn;
			m = mm;
			a.assign(n, 0);
		}

	void addEdge(int node1, int node2){
		adj[node1].push_back(node2);
		adj[node2].push_back(node1);
	}



	int count_reachable_leaves(int node, int consequtive, int parent){
		if(a[node-1] == 1){
			consequtive += 1;
			if(consequtive == (m+1)){
				return 0;
			}
		}
		else{
			consequtive = 0;
		}

		bool is_leaf = true;
		int reachable_count = 0;

		for(int child: adj[node]){
			if(child != parent){
				is_leaf = false;
				reachable_count += count_reachable_leaves(child, consequtive, node);
			}
		}

		if(is_leaf == true){
			reachable_count = 1;
		}

		return reachable_count;
	}
};


int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL); 
	
	int n, m;
	cin >> n >> m;

	Tree tree(n, m);

	// int arr[n];

	for(int i=0; i<n; i++){
		cin >> tree.a[i];
	}

	int x, y;
	for(int i=0; i<n-1; i++){
		cin >> x >> y;
		tree.addEdge(x, y);
	}

	int res = tree.count_reachable_leaves(1, 0, -1);
	cout << res << "\n";


	return 0;
}