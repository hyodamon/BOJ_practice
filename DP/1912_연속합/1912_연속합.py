import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [A[0]]

for i in range(1, N) :
    dp.append(max(A[i] + max(A[i-1], dp[i-1]), A[i]))
    
print(max(dp))