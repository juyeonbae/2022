#예제 33p

class Node:
    def __init__(self,name,left=None, right=None):
        self.name = name
        self.left= left
        self.right = right

def map():
    n1 = Node('H')
    n2 = Node('F')
    n3 = Node('S')
    n4 = Node('U')
    n5 = Node('E')
    n6 = Node('Z')
    n7 = Node('K')
    n8 = Node('N')
    n9 = Node('A')
    n10 = Node('Y')
    n11 = Node('T')
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n4.left = n8
    n5.left = n9
    n7.right = n10
    n9.right = n11
    return n1

def A_course(n):
    if n != None:
        print(n.name,'->', end='') #섬 n 방문
        A_course(n.left) #n의 왼쪽으로 진행
        A_course(n.right) #n의 오른쪽으로 진행
        
start = map()
print('A코스:\t',end='')
A_course(start)
