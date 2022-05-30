import sys

a1 = sys.stdin.readline().strip()
a2 = sys.stdin.readline().strip()
dp = [[0 for i in range(len(a2)+1)] for j in range(len(a1)+1)]

for i in range(1, len(a1)+1) :
    for j in range(1, len(a2)+1) :
        if a1[i-1] == a2[j-1] :
            dp[i][j] = dp[i-1][j-1] + 1
        else :
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
print(dp[-1][-1])
        