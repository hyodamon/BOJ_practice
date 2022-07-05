import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def BFS() :
    answer = 1
    rotate = 0
    q = deque()
    q.append((r, c, d))
    map[r][c] = 1
    while q :
        x, y, D = q.popleft()
        print("\n\n현재 위치 : (", x , ",", y, ") 방향 : ", D)
        for i in range(N) :
            print("")
            for j in range(M) :
                print(map[i][j], end=' ')

        if D == 0 :
            nx, ny, nD, bx, by = x - 1, y, 3, x + 1, y
        elif D == 1 :
            nx, ny, nD, bx, by = x, y + 1, 0, x, y - 1
        elif D == 2 :
            nx, ny, nD, bx, by = x + 1, y, 1, x - 1, y
        elif D == 3 :
            nx, ny, nD, bx, by = x, y - 1, 2, x, y + 1
        
        if 0 <= nx < N and 0 <= ny < M :
            if map[nx][ny] == 0 :
                map[nx][ny] = 1
                q.append((nx, ny, nD))
            else :
                if rotate == 4 :
                    if map[bx][by] == 1 :
                        break
                    else :
                        q.append((bx, by, nD))
                rotate += 1
                q.append((x, y, nD))
    return answer
print(BFS())