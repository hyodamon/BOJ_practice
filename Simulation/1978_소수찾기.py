import sys
input = sys.stdin.readline

N = input()
nums = list(map(int, input().split()))
answer = 0

def isSosu(n) :
    if n == 1 :
        return 0
    elif n == 2 or n == 3:
        return 1
    
    for i in range(2, (n // 2) + 1) :
        if n % i == 0 :
            return 0
    return 1


for n in nums :
    answer += isSosu(n)
    
    
print(answer)