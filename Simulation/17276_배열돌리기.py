import sys
from collections import deque
T = int(sys.stdin.readline())

for _ in range(T) :
    N, D = map(int, sys.stdin.readline().split())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    rotate = (D // 45) % 8
    N -= 1
    for r in range(rotate) :
        prev_list = deque()
        for i in range(N + 1):  # 주대각선
            prev_list.append(arr[i][i])

        for i in range(N + 1):  # 주대각선 -> 가운데열
            prev_temp = arr[i][(N + 1) // 2]
            arr[i][(N + 1) // 2] = prev_list[i]
            prev_list[i] = prev_temp

        for i in range(N + 1):  # 가운대열 -> 부대각선
            prev_temp = arr[i][N - i]
            arr[i][N - i] = prev_list[i]
            prev_list[i] = prev_temp

        for i in range(N + 1):  # 부대각선 -> 가운데행
            prev_temp = arr[(N + 1) // 2][N - i]
            arr[(N + 1) // 2][N - i] = prev_list[i]
            prev_list[i] = prev_temp

        for i in range(N + 1):  # 가운데행 -> 주대각선
            arr[N - i][N - i] = prev_list[i]
            
    for i in range(N+1) :
        for j in range(N+1) :
            print(arr[i][j], end=" ")
        print("")
                