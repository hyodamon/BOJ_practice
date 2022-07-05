import sys

calFormular = list(sys.stdin.readline().split('-')) # '-'를 기준으로 끊어가며, 입력

result = 0 # 결과값 저장
print(calFormular)
for i in range(len(calFormular)) :
    if calFormular[i].isdigit() : # 현재 선택된 것이 숫자라면, = 음수
        tmp = int(calFormular[i]) # 숫자로 저장
    else : # 숫자가 아니라면, = 수식이 포함 된
        tmp = sum(map(int, calFormular[i].split('+')))  # '+'로 끊어서 더하기
     
    if i == 0 : # 맨 앞에 것은 그대로 두고
        result += tmp
    else : # 뒤에꺼는 다 빼준다.
        result -= tmp
        
print(result)
