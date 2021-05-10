# Function should return True/False or 1/0
# Graph(graph) is a defaultict of type List
# n is no of Vertices

from collections import defaultdict


def isCyclicUtil(graph, v, visited, recStack):

    # Mark current node as visited and
    # adds to recursion stack
    visited[v] = True
    recStack[v] = True

    # Recur for all neighbours
    # if any neighbour is visited and in
    # recStack then graph is cyclic
    for neighbour in graph[v]:
        if visited[neighbour] == False:
            if isCyclicUtil(graph, neighbour, visited, recStack) == True:
                return True
        elif recStack[neighbour] == True:
            return True

    # The node needs to be poped from
    # recursion stack before function ends
    recStack[v] = False
    return False

# Returns true if graph is cyclic else false


def isCyclic(N, graph):
    visited = [False] * N
    recStack = [False] * N
    for node in range(N):
        if visited[node] == False:
            if isCyclicUtil(graph, node, visited, recStack) == True:
                return True
    return False


# {
#  Driver Code Starts


def creategraph(n, arr, graph):
    i = 0
    while i < 2 * e:
        graph[arr[i]].append(arr[i + 1])
        # graph[arr[i + 1]].append(arr[i])
        i += 2


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, e = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        graph = defaultdict(list)
        creategraph(e, arr, graph)
        if isCyclic(n, graph):
            print(1)
        else:
            print(0)
# } Driver Code Ends
