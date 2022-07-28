#AVL 트리
''' AVL 트리는 임의의 노드 n에 대해 n의 왼쪽 서브트리의 높이와
오른쪽 서브트리의 높이 차이가 1을 넘지 않는 이진탐색트리이다.

N개의 노드를 가진 AVL트리의 높이는 O(logN)이다. '''

class Node:
    def __init__ (self,key,value,height,left=None,right=None):
        self.key = key
        self.value = value
        self.height = height
        self.left = left
        self.right = right

class AVL:
    def __init__(self):
        self.root = None

    def preorder(self,n): #전위순회
        if n != None:
            print(str(n.value),' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self,n): #중위순회 
        if n!=None:
            if n.left:
                self.inorder(n.left)
            print(str(n.value),' ',end='')
            if n.right:
                self.inorder(n.right)

    def height(self,n):
        if n == None:
            return 0
        return n.height

    def put(self,key,value): #삽입 연산
        self.root = self.put_item(self.root,key,value)

    def put_item(self,n,key,value):
        if n == None:
            return Node(key,value,1)
        if n.key > key :
            n.left = self.put_item(n.left,key,value)
        elif n.key < key :
            n.right = self.put_item(n.right,key,value)
        else:
            n.value = value
            return n
        n.height = max(self.height(n.left),self.height(n.right))
        return self.balance(n)

    def balance(self, n): #불균형 처리 
        if self.bf(n) > 1:
            if self.bf(n.left) < 0:
                n.left = self.rotate_left(n.left)
            n = self.rotate_right(n)

        elif self.bf(n) < -1:
            if self.bf(n.right) > 0:
                n.right = self.rotate_right(n.right)
            n = self.rotate_left(n)
        return n

    def bf(self,n): #bf 계산
        return self.height(n.left) - self.height(n.right)
    

t=AVL()
t.put(500,'apple')
t.put(600,'banana')
t.put(200,'melon')
t.put(100,'orange')
t.put(400,'lime')
t.put(250,'kiwi')
t.put(150,'grape')
t.put(800,'peach')
t.put(700,'cherry')
t.put(50,'pear')
t.put(350,'lemon')
t.put(10,'plum')
print('전위순회:',end='')
t.preorder(t.root)
print('\n중위순회:',end='')
t.inorder(t.root)

