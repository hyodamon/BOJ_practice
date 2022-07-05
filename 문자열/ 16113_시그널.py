import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
signal = input().rstrip()
decoding = deque()
answer = ''

tmp = deque()
for i in range(N) :
    tmp.append(signal[i])   
    if (i + 1) % (N // 5) == 0 :
        tmp.append('.')
        decoding.append(tmp)
        tmp = deque()
cnt = 0
# print(decoding)
for i in range(N // 5 + 1) :
    finish = 0
    for j in range(5) :
        if decoding[j][i] == '.' :
            finish += 1
        else :
            cnt += 1
    
    if finish == 5 : # 한 숫자가 끝났을 때
        if cnt == 5 : # 전체가 5면 1
            answer += '1'
        elif cnt == 9 :
            answer += '4'
        elif cnt == 7 :
            answer += '7'
        elif cnt == 13 :
            answer += '8'
        elif cnt == 11 :
            if decoding[1][i-1] == '.' :
                answer += '5'
            elif decoding[3][i-1] == '.' :
                answer += '2'
            else :
                answer += '3'
        elif cnt == 12 :
            if decoding[1][i-1] == '.' :
                answer += '6'
            elif decoding[2][i-2] == '.' :
                answer += '0' 
            else :
                answer += '9'
        cnt = 0
        
print(answer)