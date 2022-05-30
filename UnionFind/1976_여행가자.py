import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [x for x in range(N)]

connection = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

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
        
for i in range(N) :
    for j in range(N) : 
        if connection[i][j] == 1 :
            union(i, j)
            
plan = list(map(int, sys.stdin.readline().split()))

result = 0
tmp = 0
for i in range(0, len(plan)) :
    if i == 0 or graph[plan[i]-1] == tmp :
        result = 1
    else :
        result = 0
        break
    tmp = graph[plan[i]-1]
    
if result == 1 : 
    print("YES")
else :
    print("NO")