import sys
from collections import deque
N = int(sys.stdin.readline())

for _ in range(N) :
    M, Q = map(int, sys.stdin.readline().split())
    printer = deque(list(map(int, sys.stdin.readline().split())))
    answer = 0
    while printer :
        MAX = max(printer)
        A = printer.popleft()
        Q -= 1
        
        if A == MAX :
            answer += 1
            if Q < 0 :
                print(answer)
                break
        else :
            printer.append(A)
            if Q < 0 :
                Q = len(printer) - 1