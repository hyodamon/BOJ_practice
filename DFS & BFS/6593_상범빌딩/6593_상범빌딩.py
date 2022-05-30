from collections import deque
import sys

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

def bfs(x, y, z):
    queue = deque()
    queue.append([x, y, z])
    visited[x][y][z] = 1
    while queue:
        x, y, z = queue.popleft()
        print("x, y, z : ", x, y, z)
        print("visited : ", visited)
        for i in range(6):
            nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]
            if 0 <= nx < L and 0 <= ny < R and 0 <= nz < C:
                if building[nx][ny][nz] == 'E': # 출구를 찾았을 경우
                    print("Escaped in",  visited[x][y][z], "minute(s).")
                    return
                if building[nx][ny][nz] == '.' and visited[nx][ny][nz] == 0: # 이동할 수 있고, 방문하지 않았을 경우
                    
                    visited[nx][ny][nz] = visited[x][y][z] + 1
                    queue.append([nx, ny, nz])
    print("Trapped!") # 더 이상 이동할 곳이 없을 때
                    
while 1:
    L, R, C = map(int, sys.stdin.readline().split())
    
    if L == 0 and R == 0 and C == 0: # 0 0 0 입력하면 종료
        break
    
    building = [[[] * C for _ in range(R)] for _ in range(L)] # 빌딩
    visited = [[[0 ]* C for _ in range(R)] for _ in range(L)] # 방문을 확인 할 visited
    
    for i in range(L): 
        building[i] = [list(map(str, sys.stdin.readline().strip())) for _ in range(R)]
        sys.stdin.readline()
    
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    bfs(i, j, k)