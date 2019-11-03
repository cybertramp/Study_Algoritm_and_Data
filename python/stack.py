#-*- coding: utf-8 -*-

# For Stack

'''
스택은 LIFO(Last In First Out)이다.
파이썬에서는 맨 위의 위치를 알고 있어야 한다.

2개를 넣었다면 
    stack.append(0)
    stack.append(1)
    [0],[1]이 찼으니 top=1이 되어야 한다.

1개를 뺀다면
    | 0 1 | => | 0 |
    stack.pop()을 사용하면 맨 끝에 원소를 뺀다.

'''
stack = []
for i in range(10):
    stack.append(i)

print(stack)
print('top 위치:',len(stack))

for i in range(5):
    print('꺼낸값:',stack.pop())

print(stack)
print('top 위치:',len(stack))

for i in range(4):
    print('꺼낸값:',stack.pop())

print(stack)
print('top 위치:',len(stack))

print('꺼낸값:',stack.pop())

print(stack)
print('top 위치:',len(stack))

# 스택이 비었는지에 대한 확인
if len(stack) is 0:
    print("stack is empty!")