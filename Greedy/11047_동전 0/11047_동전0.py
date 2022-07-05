import sys

N, K  = map(int, sys.stdin.readline().split()) # N : 동전의 종류, K : 구해야 할 합
coins = [int(sys.stdin.readline()) for _ in range(N)] # 동전 종류 입력
coins.sort(reverse=True) # 큰 수부터 탐색해야 하므로, 거꾸로

cnt = 0 # 동전 개수 저장
while K != 0 : # K가 0이 될 때까지,
    for coin in coins : # 코인들을 탐색해가며
        if K >= coin : # 만약 K가 현재 코인보다 크다면
            K = K - coin # 그 코인의 값만큼 빼준다.
            cnt += 1 # 동전을 사용했으므로 개수 추가
            break # 다시 탐색

print(cnt)