import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = []
for _ in range(0, M):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append([c, a-1, b-1])

minCost = 0
parent = [0] * N

for i in range(N):
    parent[i] = i


def find(node):
    if parent[node] != node:
        return find(parent[node])
    return node


def union(node1, node2):
    print(parent)
    node1 = find(node1)
    node2 = find(node2)
    if node1 < node2:
        parent[node2] = node1
    else:
        parent[node1] = node2


edges.sort()
print(edges)
for edge in edges:
    cost, node1, node2 = edge
    if find(node1) != find(node2):
        union(node1, node2)
        minCost += cost
print(parent)
print(minCost)
