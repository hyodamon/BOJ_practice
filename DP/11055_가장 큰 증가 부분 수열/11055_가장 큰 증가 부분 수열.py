import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [A[0]]

for i in range(1, N) :
    dp.append(A[i])
    for j in range(i) :
        if A[i] > A[j] :
            dp[i] = max(dp[j] + A[i], dp[i])
            
print(max(dp))