import sys

T = sys.stdin.readline().rstrip()
P = sys.stdin.readline().rstrip()
L = [-1 for _ in range(27)]
n, m = len(T), len(P)

intermediate = []
result = []

def LastOccurrenceFunc(P) :
    for i in range(0, len(P)) :
        if P[i] == 'X' :
            L[-1] = i
        L[ord(P[i]) - 97] = i
        
def BoyerMooreMatch(T, P, S = 26) :
    i = m - 1
    j = m - 1
    tmp = 0
    while True : # do-while
        print("i :", i, "j :", j)
        print("T[i] :", T[i], "P[j] :", P[j])
            
        if T[i] == P[j] or P[j] == 'X':
            if j == 0 :
                result.append(i)
                intermediate.append(1)
                i += m
                j = m-1
                tmp = 0
            else :
                if P[j] == 'X' :
                    tmp += 1
                i -= 1
                j -= 1
        else :
            tmp_i = i
            tmp_j = j
            l = L[ord(T[i]) - 97]
            print("T[i] :", T[i], "l :", l)
            if j > 1 + l : # case 2 : 현재 j보다 
                i += m - (1 + l)
                if l == -1 :
                    i -= tmp
            else :
                i += m - j
                
            j = m - 1
            intermediate.append(i - tmp_i - (m - 1 - tmp_j))
            tmp = 0
        if i > n - 1 :
            break
                
LastOccurrenceFunc()
BoyerMooreMatch()

print(intermediate)
print(result)
  
        