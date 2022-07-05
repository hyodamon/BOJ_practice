import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
words = set()
for _ in range(N) :
    words.add(input().rstrip())
Xarr = words.copy()
for word1 in words:
    for word2 in words:
        if len(word1) > len(word2) :
            if word1[:len(word2)] == word2 :
                Xarr.discard(word2)
print(len(Xarr))