import sys
from collections import deque

input = sys.stdin.readline

N, B = map(int, input().split())
number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
answer = []
def conversion(n) :
    if n // B == 0 :
        answer.append(number[n])
        return 
    else :
        answer.append(number[n % B])
        return conversion(n // B)

conversion(N)
print(''.join(answer)[::-1])