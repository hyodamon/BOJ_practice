import sys

a1 = sys.stdin.readline().strip()
a2 = sys.stdin.readline().strip()
np = [[0 for i in range(len(a2))] for j in range(len(a1))]

for i in range(len(a1)) :
    for j in range(len(a2)) :
        if a1[i] == a2[j] :
            np[i][j] = 1


dp = []

for k in range(len(a1)) :
    cnt = 0
    tmp = -1
    for i in range(k, len(a1)) :
        for j in range(len(a2)) :
            if j > tmp and np[i][j] == 1 :
                tmp = j
                cnt += 1
                break
    dp.append(cnt)
        
print(max(dp))
        