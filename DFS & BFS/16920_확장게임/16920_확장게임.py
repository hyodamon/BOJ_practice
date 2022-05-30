import sys
from collections import deque

N, M, P = map(int, sys.stdin.readline().split())
S = list(map(int, sys.stdin.readline().split()))

graph = []
for _ in range(N) : 
    graph.append(list(filter(lambda x : x != '\n', sys.stdin.readline())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def initialSetting(graph, num, power) :
    tmp = [[0 for _ in range(M)] for _ in range(N)]
    position = []
    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == str(num) :
                tmp[i][j] = num
                position.append((i, j, 1))
            elif graph[i][j] == '.' :
                tmp[i][j] = 0
            else :
                tmp[i][j] = -1
    return tmp, position, power

def bfs(value) :
    space = value[0]
    position = value[1]
    power = value[2]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    for i in position :
        visited[i[0]][i[1]] = 1
    queue = deque()
    for i in position :
        queue.append(i)
    while queue:
        x, y, cnt = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visited[x][y] != 0 and visited[nx][ny] == 0 and space[nx][ny] != -1:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny, cnt+1))
    return visited

players = []
for i in range(P) :
    players.append(bfs(initialSetting(graph, i+1, S[i])))

maxCnt = max(map(max, map(max, players)))
tmp2 = [[0 for _ in range(M)] for _ in range(N)]

for cnt in range(1, maxCnt+1) :
    for i in range(N) :
        for j in range(M) :
            for k in range(0, P) :
                if players[k][i][j] == cnt and tmp2[i][j] == 0 :
                    tmp2[i][j] = k+1
                    
for k in range(0, P) :
    cnt = 0
    for i in range(N) :
        for j in range(M) :
            if tmp2[i][j] == k+1 :
                cnt = cnt + 1
    print(cnt, end=' ')