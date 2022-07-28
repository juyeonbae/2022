#이진트리

class Node:
    def __init__(self,item, left=None,right=None):
        self.item = item
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self,n): #전위순회
        if n != None:
            print(str(n.item),' ',end='')
            if n.left:
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)

    def inorder(self,n): #중위순회 
        if n!=None:
            if n.left:
                self.inorder(n.left)
            print(str(n.item),' ',end='')
            if n.right:
                self.inorder(n.right)

    def postorder(self,n): #후위순회 
        if n!=None:
            if n.left:
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.item),' ',end='')

    def levelorder(self,root): #레벨순회
        q=[]
        q.append(root)
        while len(q) != 0:
            t = q.pop(0)
            print(str(t.item),' ',end='')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)

    def height(self,root): #트리 높이 계산 
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right))+1
    #두 자식노드의 높이 중 큰 높이 +1



t=BinaryTree()
n1 = Node(100)
n2 = Node(200)
n3 = Node(300)
n4 = Node(400)
n5 = Node(500)
n6 = Node(600)
n7 = Node(700)
n8 = Node(800)
n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
n4.left = n8
t.root = n1
print('tree height =',t.height(t.root))
print('preorder = ',end='')
t.preorder(t.root)
print('\ninorder = ',end='')
t.inorder(t.root)
print('\npostorder = ',end='')
t.postorder(t.root)
print('\nlevelorder = ',end='')
t.levelorder(t.root)
