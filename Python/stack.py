class Node:
    def __init__(self=None,data=None,link=None):
        self.data = data
        self.prev = link

class Stack:
    def __init__(self):
        self.top = None

    def push(self,data):
        new_node = Node(data,self.top)
        self.top = new_node

    def pop(self):
        data = self.top.data
        self.top = self.top.prev
        return data

    def print(self):
        p = self.top
        while p != None:
            print(p.data)
            p = p.prev

f = Stack()
f.push("apple")
f.print()
f.push("cherry")
f.print()
f.push("pear")
f.print()

