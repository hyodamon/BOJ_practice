import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
F = [0 for _ in range(len(P))]
n, m = len(T), len(P)

intermediate = []
result = []

def failureFunc() :
    i = 1
    j = 0
    while i < len(P) :
        if P[i] == P[j] :
            F[i] = j+1
            i += 1
            j += 1
        elif j > 0 :
            j = F[j-1]
        else :
            F[i] = 0
            i += 1
    print(F[0], F[1], F[2])

def KMP() :
    failureFunc()
    i = 0
    j = 0
    while i < n :
        if T[i] == P[j] :
            if j == m - 1 :
                intermediate.append(m - F[j])
                result.append(i-j)
                i += 1 - F[j]
                j = 0
            else : 
                i += 1
                j += 1
        elif j > 0 :
            intermediate.append(j - F[j-1])
            j = F[j-1]
        else :
            intermediate.append(1)
            i += 1
    
KMP()
print(intermediate)
print(result)