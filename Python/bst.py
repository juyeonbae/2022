class Node:
    def __init__(self,key,value,left=None,right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

class BST:
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

    def get(self,key): #탐색 연산
        return self.get_item(self.root,key)

    def get_item(self,n,k):
        if n == None:
            return None
        if n.key > k:
            return self.get_item(n.left,k) #왼쪽 서브트리 탐색 
        elif n.key < k:
            return self.get_item(n.right,k) #오른쪽 서브트리 탐색 
        else:
            return n.value #탐색 성공

    def put(self,key,value): #삽입 연산
        self.root = self.put_item(self.root,key,value)

    def put_item(self,n,key,value):
        if n == None:
            return Node(key,value)
        if n.key > key:
            n.left = self.put_item(n.left,key,value)
        elif n.key < key:
            n.right = self.put_item(n.right,key,value)
        else:
            n.value = value
        return n

    def min(self): #최솟값 찾는 연산
        if self.root == None:
            return None
        return self.minimum(self.root)

    def minimum(self,n):
        if n.left == None:
            return n
        return self.minimum(n.left)

    def delete_min(self,n): #최솟값 삭제 연산 
        if self.root == None:
            print('empty')
        self.root = self.del_min(self.root)

    def del_min(self, n):
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n

    def delete(self,k): #삭제 연산
        self.root = self.del_node(self.root,k) #루트와 del_node()가 리턴하는 노드를 재연결

    def del_node(self,n,k):
        if n == None:
            return None
        if n.key > k:
            n.left = self.del_node(n.left,k) #n의 왼쪽자식과 del_node()가 리턴하는 노드 재연결
        elif n.key < k:
            n.right = self.del_node(n.right,k) #n의 오른쪽자식과 del_node()가 리턴하는 노드 재연결
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            target = n  #target은 삭제될 노드 
            n = self.minimum(target.right) #target의 중위 후속자를 찾아 n이 참조하게 함 
            n.right = self.del_min(target.right) #n의 오른쪽자식과 target의 오른쪽자식 연결 
            n.left = target.left #n의 왼쪽자식과 target의 왼쪽자식 연결 
        return n
    

t=BST()
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
print('\n250: ',t.get(250))
t.delete(200)
print('200삭제 후')
print('\n전위순회:',end='')
t.preorder(t.root)
print('\n중위순회:',end='')
t.inorder(t.root)
