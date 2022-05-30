import sys

N = int(sys.stdin.readline())
lines = []
ans = 0

for _ in range(N):
    height = int(sys.stdin.readline().strip())
    
    while lines and lines[-1][0] < height:
        ans+= lines.pop()[1]
        
    if lines and lines[-1][0] == height:
        cnt = lines.pop()[1]
        ans += cnt
        if len(lines) != 0 :
            ans += 1
        lines.append((height, cnt+1))
        
    else:
        if len(lines) != 0 :
            ans += 1
        lines.append((height, 1))
    
print(ans)