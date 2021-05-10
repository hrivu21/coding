def isCyclicUtil(graph, v, visited, recStack, parent):
    visited[v] = True
    recStack[v] = True

    for neighbour in graph[v]: 
        if neighbour == parent:
            continue
        if visited[neighbour] is False:
            if isCyclicUtil(graph, neighbour, visited, recStack, v) is True:
                return True
        elif recStack[neighbour] is True:
            return True

    recStack[v] = False
    return False


def isCyclic(graph, N):
    visited = [False] * N
    recStack = [False] * N
    for node in range(N):

        if visited[node] is False:
            if isCyclicUtil(graph, node, visited, recStack, -1) is True:
                return 1
    return 0



#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from collections import defaultdict

#Contributed by : Nagendra Jha

#Graph Class:
class Graph():
    def __init__(self,vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def addEdge(self,u,v): # add directed edge from u to v.
        self.graph[u].append(v)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        N,E = map(int,input().strip().split())
        g = Graph(N)
        edges = list(map(int,input().strip().split()))

        for i in range(0,len(edges),2):
            u,v = edges[i],edges[i+1]
            g.addEdge(u,v) # add an undirected edge from u to v
            g.addEdge(v,u)
        print(isCyclic(g.graph,N))
# } Driver Code Ends