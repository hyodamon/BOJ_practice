import sys
input = sys.stdin.readline

N, B = input().split()
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

answer = 0
j = 0
for i in range(len(N)-1, -1, -1) :
    if '0' <= N[i] <= '9' :
        tmp = int(N[i])
    else :
        tmp = ord(N[i]) - 55
    answer += tmp * (int(B) ** i)
    j += 1
print(answer)