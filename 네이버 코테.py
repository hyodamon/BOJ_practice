import sys

A = list(map(int, sys.stdin.readline().split()));
K = int(sys.stdin.readline())

def solution() :
    answer = 0;
    arr = []
    prev = A[0]; # 이전 A의 요소
    
    for i in range(1, len(A)) :
        arr.append(abs(A[i] - prev))
        prev = A[i]
        
    _max = max(A)
    _min = min(A)
     
    while (K != 0) :
        
        
            
    return answer
    
solution()
print(A)