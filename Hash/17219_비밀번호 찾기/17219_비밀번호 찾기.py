import sys

N, M = map(int, sys.stdin.readline().split())
notepad = {}

for _ in range(N):
    addr, pw = sys.stdin.readline().split()
    notepad[addr] = pw

for _ in range(M):
    find = sys.stdin.readline()
    print(notepad[find.strip('\n')])
