#단순연결리스트로 구현한 스택

class Node:
    def __init__(self,item,link):
        self.item = item
        self.next = link

def push(item):
    global top
    global size
    top = Node(item,top) #새 노드 객체를 생성하여 연결리스트의 첫 노드로 삽입 
    size += 1

def peek():
    if size != 0:
        return top.item     #top 항목만 리턴 

def pop():
    global top  #전역변수 
    global size
    if size != 0:
        top_item = top.item
        top = top.next      #연결리스트에서 top이 참조하던 노드 분리시킴
        size -= 1
        return top_item     #제거된 top항목 리턴 

def print_stack():
    print('top ->\t', end='')
    p = top
    while p:
        if p.next != None:
            print(p.item,'->',end='')
        else:
            print(p.item, end='')
        p = p.next
    print()

top = None
size = 0
push('apple')
push('orange')
push('cherry')
print_stack()
print(peek())
print_stack()
push('pear')
print_stack()
pop()
print(peek())
print_stack()
pop()
print(peek())
print_stack()
pop()
print(peek())
print_stack()
pop()
print(peek())
print_stack()
