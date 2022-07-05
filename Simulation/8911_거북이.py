import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    answer = 0
    command = input().rstrip()
    now = [0, 0]
    d = [0, 1]
    minX = 0
    minY = 0
    maxX = 0
    maxY = 0
    
    for c in command :
        if c == 'F' :
            now[0] += d[0]
            now[1] += d[1]
        elif c == 'B' :
            now[0] -= d[0]
            now[1] -= d[1]
        elif c == 'L' :
            if d == [0, 1] :
                d = [-1, 0]
            elif d == [-1, 0] :
                d = [0, -1]
            elif d == [0, -1] :
                d = [1, 0]
            else :
                d = [0, 1]
        else :
            if d == [0, 1] :
                d = [1, 0]
            elif d == [1, 0] :
                d = [0, -1]
            elif d == [0, -1] :
                d = [-1, 0]
            else :
                d = [0, 1]
        if now[0] < minX :
            minX = now[0]
        if now[0] > maxX :
            maxX = now[0]
        if now[1] < minY :
            minY = now[1]
        if now[1] > maxY :
            maxY = now[1]
    print((maxX - minX) * (maxY - minY))