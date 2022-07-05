import sys
from collections import deque

declare = sys.stdin.readline().rstrip(';').split(' ')
result = deque()
for i in range(1, len(declare)) :
    variable = ''
    type = ''
    for c in range(0, len(declare[i])) :
        if 65 <= ord(declare[i][c]) <= 90 or 97 <= ord(declare[i][c]) <= 122 :
            variable += declare[i][c]
        elif declare[i][c] != ',' and declare[i][c] != ']':
            if declare[i][c] == '[' :
                type += ']'
            type += declare[i][c]
    result.append(type[::-1] + ' ' + variable)
# print(result)
for i in range(len(result)) :
    print("%s%s;"%(declare[0], result[i]))