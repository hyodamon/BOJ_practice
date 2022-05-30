import sys

N, M = map(int, sys.stdin.readline().split())

dogam = {}

for i in range(N):
    pokemon = sys.stdin.readline().strip('\n')
    dogam[pokemon] = i

reverse_dogam = dict(map(reversed, dogam.items()))

for i in range(M):
    Q = sys.stdin.readline().strip('\n')
    if ord(Q[0]) >= 48 and ord(Q[0]) <= 57:
        print(reverse_dogam[int(Q)-1])
    else:
        print(dogam[Q]+1)
