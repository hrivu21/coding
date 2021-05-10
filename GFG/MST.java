// Initial Template for Java

import java.util.*;
import java.io.*;
import java.lang.*;

  public class Driver_class {

    public static void main(String args[]) throws IOException {

        BufferedReader read =
            new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(read.readLine());
        while (t-- > 0) {
            String str[] = read.readLine().trim().split(" ");
            int V = Integer.parseInt(str[0]);
            int E = Integer.parseInt(str[1]);

            ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
            for (int i = 0; i < V; i++) {
                ArrayList<Integer> temp = new ArrayList<>();
                for (int j = 0; j < V; j++) temp.add(Integer.MAX_VALUE);
                graph.add(temp);
            }
            str = read.readLine().trim().split(" ");
            int k = 0;
            int i=0;
            while (i++<E) {
                int u = Integer.parseInt(str[k++]);
                int v = Integer.parseInt(str[k++]);
                int w = Integer.parseInt(str[k++]);
                u--;
                v--;
                graph.get(u).set(v, w);
                graph.get(v).set(u, w);
            }

            System.out.println(new MST().spanningTree(V, E, graph));
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class MST {
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


    static int spanningTree(int V, int E, ArrayList<ArrayList<Integer>> graph) {
        boolean[] nodesIncluded = new boolean[V];
        int[] mst = new int[V];

        int cost = 0;

        int[] key = new int[V];
        for(int i=0; i<V; i++){
            key[i] = Integer.MAX_VALUE;
            nodesIncluded[i] = false;
        }

        key[0] = 0;

        for(int nodeCount=0; nodeCount<V; nodeCount++){

            int currVertex = minkey(key, nodesIncluded);
            nodesIncluded[currVertex] = true;
            cost += key[currVertex];

            for(int i = 0; i<V; i++){
                if(graph.get(currVertex).get(i) > 0 && nodesIncluded[i] == false){
                    if(graph.get(currVertex).get(i) < key[i])
                    key[i] = graph.get(currVertex).get(i);
                }
            }
        }
        return cost;
    }
    
}
