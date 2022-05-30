import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [1]

for i in range(1, N) :
    dp.append(1)
    for j in range(i) :
        if A[i] > A[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1
print(dp)