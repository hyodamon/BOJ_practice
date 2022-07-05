import sys
from collections import deque

string = sys.stdin.readline()
stack = deque()
result = deque()
answer = 0

if len(string) > 1 :
    for char in string :
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack[-1] == '[' :
                stack = deque([0])
                break
            elif stack[-1] == '(' :
                stack.pop()
                stack.append(2)                
            elif type(stack[-1]) == int :
                num = stack.pop() * 2
                stack.pop()
                if stack and type(stack[-1]) == int :
                    num += stack.pop()
                stack.append(num)
        elif char == ']' :
            if len(stack) == 0 or stack[-1] == '(' :
                stack = deque([0])
                break
            elif stack[-1] == '[' :
                stack.pop()
                stack.append(3)
            elif type(stack[-1]) == int :
                num = stack.pop() * 3
                stack.pop()
                if stack and type(stack[-1]) == int :
                    num += stack.pop()
                stack.append(num)
    if type(stack[0]) == int :
        answer = sum(stack)
    else :
        answer = 0
else :
    answer = 0

print(answer)