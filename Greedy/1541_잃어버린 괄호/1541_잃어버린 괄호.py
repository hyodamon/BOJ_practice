import sys

calFormular = list(sys.stdin.readline().split('-'))

result = 0
for i in range(len(calFormular)) :
    if calFormular[i].isdigit() :
        tmp = int(calFormular[i])
    else :
        tmp = sum(map(int, calFormular[i].split('+')))
    
    if i == 0 :
        result += tmp
    else :
        result -= tmp
        
print(result)
