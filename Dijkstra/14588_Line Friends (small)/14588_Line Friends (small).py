import sys

N = int(sys.stdin.readline())  # 선분 수

board = [[float("inf") for j in range(N)] for i in range(N)]  # 그래프
lines = [list(map(int, sys.stdin.readline().split()))
         for _ in range(N)]  # 선분들 좌표

for i in range(0, N):  # 받은 노드 정보들로 갱신
    board[i][i] = 0  # 자기 자신은 0
    for j in range(i+1, N):
        if (lines[j][0] >= lines[i][0] and lines[j][0] <= lines[i][1]) or (lines[j][1] >= lines[i][0] and lines[j][1] <= lines[i][1]) or (lines[j][0] <= lines[i][0] and lines[j][1] >= lines[i][1]):
            board[i][j] = 1
            board[j][i] = 1

print(board)

for k in range(0, N):  # 플루이드 알고리즘 적용
    for i in range(0, N):
        for j in range(0, N):
            if board[i][k] + board[k][j] < board[i][j]:
                board[i][j] = board[i][k] + board[k][j]

M = int(sys.stdin.readline())  # 질문 수

for i in range(M):
    x, y = map(int, sys.stdin.readline().split())
    if board[x-1][y-1] == float("inf"):  # 무한대면 -1 출력
        print(-1)
    else:
        print(board[x-1][y-1])
