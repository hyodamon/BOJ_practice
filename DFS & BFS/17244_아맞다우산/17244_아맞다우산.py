import sys
from collections import deque
N, M  = map(int, sys.stdin.readline().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

house = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(M)]
stuff = 0
visited = [[0 for _ in range(N)] for _ in range(M)]
result = deque()

print(house)
print(visited)
for i in range(M) :
    for j in range(N) :
        if house[i][j] == 'S' :
            R, C = i, j
        elif house[i][j] == 'X' :
            stuff += 1
            
def BFS() :
    q = deque()
    q.append((R, C, 0, stuff))
    
    while q :
        for i in range(M) :
            print("")
            for j in range(N) :
                print(house[i][j], end=' ')
        r, c, move, s = q.popleft()
        print(r, c, move, s)
        for i in range(4) :
            nr, nc = r + dr[i], c + dc[i]
            if s == 0 and house[nr][nc] == 'E' :
                result.append(move)
            if 0 <= nr < M and 0 <= nc < N :
                print(nr, nc)
                if visited[nr][nc] <= 2 :
                    if house[nr][nc] != '#' :
                        if house[nr][nc] == 'X' :
                            s -= 1
                        visited[nr][nc] += 1
                        q.append((nr, nc, move + 1, s))
BFS()
print(result)    
# def DFS(r, c, move, s) :
#     if s == 0 and house[r][c] == 'E' :
#         return move
    
#     for i in range(4) :
#         nr, nc = r + dr[i], c + dc[i]
#         if 0 <= nr < N and 0 <= nc < M :
#             if house[nr][nc] != '#' :
#                 if house[nr][nc] == 'X' :
#                     s -= 1
#                     house[nr][nc] == '.'    
#                 DFS(nr, nc, move + 1, s)
#     return -1
    

# print(DFS(R, C, 1, stuff))
