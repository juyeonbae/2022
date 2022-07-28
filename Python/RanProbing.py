#랜덤조사(Random Probing)

import random
class RanProbing:
    def __init__(self,size):
        self.M = size
        self.a = [None]*size
        self.d = [None]*size
        self.N = 0              #항목 수

    def hash(self,key):
        return key % self.M     #나눗셈 해시함수 
    
    def put(self,key):
        initial_position = self.hash(key) #초기값 
        i = initial_position
        random.seed(1000)                 #난수 생성 초기값 
        while True:
            if self.a[i] == None:   #빈 곳 발견 
                self.a[i] = key
                self.N += 1
                return
            if self.a[i] == key:
                return
            j = random.randint(1,99)  #난수 크기 범위 지정 
            i = (initial_position + j) % self.M
            if self.N > self.M:
                break
            
    def get(self,key):
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        random.seed(1000)
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]
            i = (initial_position + random.randint(1, 99)) % self.M
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ',end='')
        print()

t = RanProbing(13)
t.put(25)
t.put(37)
t.put(18)
t.put(55)
t.put(22)
t.put(35)
t.put(50)
t.put(63)
print("탐색 결과:")
print('50의 data = ',t.get(50))
print('63의 data = ',t.get(63))
print('해시테이블:')
t.print_table()
        
