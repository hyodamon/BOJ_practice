import sys
input = sys.stdin.readline
board = [list(map(int, input().split())) for _ in range(19)]
winner = 0

dr = [1, 1, -1, 0]
dc = [0, 1, 1, 1]

def direction(r, c, color) :
    result = []
    for i in range(4) :
        nr, nc, br, bc = r + dr[i], c + dc[i], r - dr[i], c - dc[i]
        # print((r, c), (nr, nc), "|", (br, bc))
        if 0 <= nr < 19 and 0 <= nc < 19 and board[nr][nc] == color :
            if br < 0 or br >= 19 or bc < 0 or br >= 19 or board[br][bc] != color :
                result.append((dr[i], dc[i]))
    return result

def check(r, c, color, d, move) :
    # print("색 :", color, (r, c), "칸 이동 :", move)
    nr, nc = r + d[0], c + d[1]
    if 0 <= nr < 19 and 0 <= nc < 19 :
        if board[nr][nc] == color :
            return check(nr, nc, color, d, move+1)
    return move

for i in range(19) :
    for j in range(19) :
        if board[i][j] > 0 :
            for d in direction(i, j, board[i][j]) :
                # print(check(i, j, board[i][j], d, 1))
                if check(i, j, board[i][j], d, 1) == 5 :
                    if winner == 0 or winner == board[i][j] :
                        winner = board[i][j]
                        location = [i, j]
                    else :
                        print(0)
                        sys.exit()
print(winner)           
if winner :
    print(location[0] + 1, location[1] + 1)