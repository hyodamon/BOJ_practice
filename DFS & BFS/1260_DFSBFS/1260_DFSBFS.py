import sys
from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

graph = dict()
for i in range(N):
    graph[i+1] = []

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)
    graph[start].sort()
    graph[end].sort()


def DFS(graph, start_node, visited=[]):

    visited.append(start_node)

    for node in graph[start_node]:
        if node not in visited:
            DFS(graph, node, visited)

    return visited


def BFS(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


DFS_result = DFS(graph, V)
for _ in DFS_result:
    print(_, end=" ")

print()

BFS_result = BFS(graph, V)
for _ in BFS_result:
    print(_, end=" ")
