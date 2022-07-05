import sys

a = [3, 2, 4, 4, 2, 5, 2, 5, 5]

def solution (arr) :
    answer = []
    arr.sort()
    
    cnt = 1
    for i in range(1, len(arr)) :
        if arr[i] == arr[i-1] :
            cnt += 1
        else :
            if cnt > 1 :
                answer.append(cnt)
            cnt = 1
            
    if cnt > 1 :
        answer.append(cnt)
    if len(answer) == 0 :
        answer.append(-1)
    
    return answer

print(solution(a))