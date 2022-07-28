#파이썬 리스트로 구현한 스택
#LIFO

def push(item):
    stack.append(item)

def peek():
    if len(stack) != 0:
        return stack[-1] #top항목 = 리스트의 맨 뒤 항목 리턴

def pop():
    if len(stack) != 0:
        item = stack.pop(-1)
        return item

stack = []
push('apple')
push('orange')
push('cherry')
push('grape')
print(stack)
pop()
print(stack)
