import sys
input = sys.stdin.readline
N = int(input())
candy = [list(input().rstrip()) for _ in range(N)]

def swap(r1, c1, r2, c2) :
    candy[r1][c1], candy[r2][c2] = candy[r2][c2], candy[r1][c1] 

def check() :
    result = 0
    for i in range(N-1) :
        c = 1
        for j in range(N-1) :
            if candy[i][j] == candy[i][j+1] :
                c += 1
            else :
                c = 1
            if result < c :
                result = c
        c = 1
        for j in range(N-1) :
            if candy[j][i] == candy[j+1][i] :
                c += 1
            else :
                c = 1
            if result < c :
                result = c

    return result
answer = 0
if check() == N :
    answer = N
else :
    for i in range(N) :
        for j in range(N-1) :
            if candy[i][j] != candy[i][j+1] :
                swap(i, j, i, j+1)
                cnt = check()
                if cnt == N :
                    print(cnt)
                    sys.exit()
                if answer < cnt :
                    answer = cnt
                swap(i, j+1, i, j)
            if candy[j][i] != candy[j+1][i] :
                swap(j, i, j+1, i)
                cnt = check()
                if cnt == N :
                    print(cnt)
                    sys.exit()
                if answer < cnt :
                    answer = cnt
                swap(j+1, i, j, i)
            
print(answer)