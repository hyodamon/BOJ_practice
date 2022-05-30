import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

def bfs(x, y, w):
    queue = deque()
    queue.append((x, y, w))
    while queue:
        x, y, w = queue.popleft()
        if x == N-1 and y == M-1:
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M :
                if graph[nx][ny] == 1 and w == 1: # 벽을 만나고 벽을 한번 부술 수 있는 경우
                    visited[nx][ny][0] = visited[x][y][w] + 1
                    queue.append([nx, ny, 0])
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 벽이 없고 방문한적이 없는 경우
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
            
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
visited[0][0][1] = 1

bfs(0, 0, 1)
if visited[N-1][M-1][0] != 0 :
    print(visited[N-1][M-1][0])
else :
    print(-1)