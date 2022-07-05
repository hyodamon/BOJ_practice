import sys

N = int(sys.stdin.readline())
switchs = list(map(int, sys.stdin.readline().split()))
T = int(sys.stdin.readline())

for _ in range(T) :
    s, l = map(int, sys.stdin.readline().split())
    
    if s == 1 :
        for i in range(l - 1, len(switchs), l) :
            if switchs[i] :
                switchs[i] = 0
            else :
                switchs[i] = 1
    elif s == 2 :
        if switchs[l - 1] :
                switchs[l - 1] = 0
        else :
            switchs[l - 1] = 1
        for i in range(0, len(switchs) // 2) :
            if ((l - 1) - i) >= 0 and ((l - 1) + i) < len(switchs) : 
                if switchs[(l - 1) - i] == switchs[(l - 1) + i] :               
                    if switchs[(l - 1) - i] :
                        switchs[(l - 1) - i] = 0
                    else :
                        switchs[(l - 1) - i] = 1
                    if switchs[(l - 1) + i] :
                        switchs[(l - 1) + i] = 0
                    else :
                        switchs[(l - 1) + i] = 1
                else :
                    break
            else :
                break

for i in range(len(switchs)) :
    print(switchs[i], end=" ")
    if (i + 1) % 20 == 0 :
        print()