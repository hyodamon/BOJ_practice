import sys

K, L = map(int, sys.stdin.readline().split())
nums = {}

for i in range(L):
    num = sys.stdin.readline().strip('\n')
    nums[num] = i

snums = sorted(nums.items(), key=lambda x: x[1])

for i in range(K):
    print(snums[i][0])
