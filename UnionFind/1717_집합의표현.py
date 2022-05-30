import sys
sys.setrecursionlimit(1000000)

N, M = map(int, sys.stdin.readline().split())

graph = [x for x in range(N+1)]

def find(node) :
    if graph[node] != node :
        graph[node] = find(graph[node])
    return graph[node]
    
def union(node1, node2) :
    node1_parent = find(node1)
    node2_parent = find(node2)
    if node1_parent < node2_parent:
        graph[node2_parent] = node1_parent
    else:
        graph[node1_parent] = node2_parent

# for _ in range(M) :
#     oper, a, b = map(int, sys.stdin.readline().split())

#     if oper == 0 :
#         union(a, b)
#     elif oper == 1 :
#         if find(a) == find(b) : 
#             print("YES")
#         else :
#             print("NO")
union(1, 3)
union(2, 3)
print(graph)