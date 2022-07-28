#단순연결리스트

class SList:
    class Node:
        def __init__(self,item,link):   #노드생성자항목과 다음 노드 레퍼런스 
            self.item = item
            self.next = link

    def __init__(self):     #단순연결리스트 생성자 head와 항목 수로 구성 
        self.head = None
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):     
        return self.size==0

    def insert_front(self,item):    #노드가 빈 경우 
        if self.is_empty():
            self.head = self.Node(item, None)
        else:
            self.head = self.Node(item,self.head)   #head가 새 노드 참조 
        self.size +=1

    def insert_after(self, item, p):    #새 노드가 p 다음 노드가 됨 
        p.next = SList.Node(item,p.next)
        self.size += 1

    def delete_front(self):     #empty인 경우 에러 처리 
        if self.is_empty():
            raise EmptyError('underflow')
        else:
            self.head = self.head.next  #head가 둘째 노드를 참조 
            self.size -= 1

    def delete_after(self,p):
        if self.is_empty():
            raise EmptyError('underflow')   #empty인 경우 에러 처리 
        t = p.next
        p.next = t.next     #p 다음 노드를 건너뛰어 연결 
        self.size -= 1

    def search(self, target):
        p = self.head                #head로부터 순차 탐색 
        for k in range(self.size):
            if target == p.item:
                return k+1           #탐색 성공 
            p = p.next
        return None                 #탐색 실패 

    def print_list(self):
        p = self.head
        while p:
            if p.next != None:
                print(p.item, '->',end='')
            else:
                print(p.item)
            p = p.next            #노드들을 순차탐색 

class EmptyError(Exception):      #underflow시 에러 처리 
    pass

s=SList()
s.insert_front('orange')
s.insert_front('apple')
s.insert_after('cherry',s.head.next)
s.print_list()
print('cherry는 %d번째' %s.search('cherry'))
s.delete_after(s.head)
s.print_list()
