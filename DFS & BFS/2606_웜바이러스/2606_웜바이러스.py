import sys
input = sys.stdin.readline

N = int(input())
graph = dict()
for i in range(N) :
    graph[i+1] = []

M = int(input())
for i in range(M) :
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[u].sort()
    graph[v].append(u)
    graph[v].sort()
    

def DFS(start_node, visited=[]):
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            DFS(node, visited)

    return visited
    
answer = DFS(1)
print(len(answer) - 1)
