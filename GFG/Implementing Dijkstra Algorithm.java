//Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

class Gfg
{
    static void printSolution(int dist[], int n)
    {
        for(int i = 0; i < n; i++)
            System.out.print(dist[i] + " ");
    }
    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        int t = Integer.parseInt(sc.next());
        
        while(t > 0)
        {
            int V = Integer.parseInt(sc.next());;
            ArrayList<ArrayList<Integer>> list = new ArrayList<>(V);
            for(int i = 0;i < V; i++)
            {
                ArrayList<Integer> temp = new ArrayList<>(V);
                list.add(i, temp);
            }
            
            for(int i = 0; i < V; i++)
            {
                ArrayList<Integer> temp = list.get(i);
                for(int j = 0; j < V; j++)
                {
                    temp.add(Integer.parseInt(sc.next()));
                }
                list.add(temp);
            }
            int s = Integer.parseInt(sc.next());;
            Solution T = new Solution();
            int[] res = T.dijkstra(list, s, V);
            printSolution (res, V);
            System.out.println();
            t--;
        }
    }
}// } Driver Code Ends


//User function Template for Java

/*
*   g: vector of vectors which represents the graph
*   src: source vertex to start traversing graph with
*   V: number of vertices
*/
class Solution{
    static void p(int[] a){
        for(int i=0; i<a.length; i++){
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }

    static void p(boolean[] a){
        for(int i=0; i<a.length; i++){
            System.out.print(a[i] + " ");
        }
        System.out.println();
    }


    static int minkey(int[] key, boolean[] nodesIncluded){
        int nextVertex = -1;
        int min = Integer.MAX_VALUE;

        for(int i=0; i<key.length; i++){
            if (!nodesIncluded[i]){
                if(key[i] < min){
                    min = key[i];
                    nextVertex = i;
                }
            }
        }
        return nextVertex;
    }

    static int[] dijkstra(ArrayList<ArrayList<Integer>> g, int src, int V){
        boolean[] nodesIncluded = new boolean[V];
        int[] dist = new int[V];

        for(int i=0; i<V; i++){
            dist[i] = Integer.MAX_VALUE;
            nodesIncluded[i] = false;
        }
        dist[src] = 0;

        // p(dist);
        // p(nodesIncluded);

        for(int node_count=0; node_count<V; node_count++){
            int currVertex = minkey(dist, nodesIncluded);
            // System.out.println(i +"   " + currVertex);
            nodesIncluded[currVertex] = true;

            for(int j=0; j<V; j++){
                if(g.get(currVertex).get(j) > 0 && !nodesIncluded[j] && g.get(currVertex).get(j) < dist[j]){
                    if (g.get(currVertex).get(j) + dist[currVertex] < dist[j]){
                        dist[j] = g.get(currVertex).get(j) + dist[currVertex];
                    }
                }
                // p(dist);
            }
        }
        // p(dist);
        return dist;
    }
}