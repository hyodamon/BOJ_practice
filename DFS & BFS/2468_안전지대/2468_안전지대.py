import sys
from collections import deque

N = int(sys.stdin.readline())
area = [list(map(int, input().split())) for _ in range(N)]

maxValue = 0  # 물에 잠기지 않는 안전한 영역의 최대 개수 (정답 값)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(x, y, height):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and area[nx][ny] > height and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                queue.append((nx, ny))


maxNum = 0  # 최고 높이

for i in area:
    for j in i:
        if maxNum < j:
            maxNum = j

for i in range(maxNum):
    visited = [[0] * N for _ in range(N)]
    cnt = 0  # 물에 잠기지 않는 안전한 영역의 개수
    for j in range(N):
        for k in range(N):
            if area[j][k] > i and visited[j][k] == 0:  # 높이보다 위에 있고 visited가 0이면
                bfs(j, k, i)  # x, y 좌표와 높이
                cnt = cnt + 1
    maxValue = max(maxValue, cnt)

print(maxValue)
