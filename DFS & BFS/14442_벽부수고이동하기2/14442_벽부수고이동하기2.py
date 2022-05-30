import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y, w):
    queue = deque()
    queue.append((x, y, w)) # w는 부순 횟수
    while queue:
        x, y, w = queue.popleft()
        if x == N-1 and y == M-1: # 마지막 자리까지 갔을 때 끝내기
            return visited[x][y][w]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny][w] == 0:
                if graph[nx][ny] == 1 and w < K: # 벽을 만나고 벽을 부술 수가 기회(K)보다 작은 경우
                    visited[nx][ny][w+1] = visited[x][y][w] + 1 # 부순 횟수(w) 추가
                    queue.append([nx, ny, w+1]) 
                elif graph[nx][ny] == 0 and visited[nx][ny][w] == 0: # 벽이 없고 방문한적이 없는 경우
                    visited[nx][ny][w] = visited[x][y][w] + 1
                    queue.append([nx, ny, w])
    return -1
            
visited = [[[0] * (K+1) for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

print(bfs(0, 0, 0))