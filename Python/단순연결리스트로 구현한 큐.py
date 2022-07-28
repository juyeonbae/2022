#단순연결리스트로 구현한 큐

class Node:
    def __init__(self,item,n):
        self.item = item
        self.next = n

def add(item):
    global size
    global front
    global rear
    newNode = Node(item,None)
    if size == 0:
        front = newNode
    else:
        rear.next = newNode
    rear = newNode
    size += 1

def remove():
    global size
    global front
    global rear
    if size != 0:
        fitem = front.item
        front = front.next
        size -= 1
        if size ==0:
            rear = None
        return fitem

def printq():
    p =front
    print('front:',end='')
    while p:
        if p.next != None:
            print(p.item,'->',end='')
        else:
            print(p.item,end='')
        p=p.next
    print(' :rear')
front = None
rear = None
size = 0

        
add('apple')
add('orange')
add('cherry')
printq()
remove()
printq()
