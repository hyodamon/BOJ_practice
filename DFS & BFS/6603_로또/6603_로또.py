import sys


def lotto(idx, cnt):
    if cnt == 6:
        for i in range(k):
            if check[i] == True:
                print(S[i], end=' ')
        print('')
    else:
        for i in range(idx, k):
            check[i] = True
            lotto(i+1, cnt+1)
            check[i] = False


while 1:
    S = list(map(int, sys.stdin.readline().split()))
    if S[0] == 0:
        break
    k = S.pop(0)

    check = [0] * k
    lotto(0, 0)
    print('')
