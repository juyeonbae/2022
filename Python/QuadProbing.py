#이차조사(Quadratic Probing)

class QuadProbing:
    def __init__(self,size):
        self.M = size
        self.a = [None]*size
        self.d = [None]*size
        self.N = 0              #항목 수

    def hash(self,key):
        return key % self.M     #나눗셈 해시함수 

    def put(self,key,data):
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:   #빈 곳 발견 
                self.a[i] = key
                self.d[i] = data
                self.N += 1
                return
            if self.a[i] == key:
                self.d[i] = data
                return
            j += 1
            i = (initial_position + j*j) % self.M #다음 원소 검사를 위해 
            if self.N > self.M: #저장된 항목 수가 테이블 크기보다 크면 저장 실패
                break

    def get(self,key): #탐색 연산 
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]    #탐색 성공 
            i = (initial_position + j*j) %self.M #다음 원소 검사를 위해 
            j += 1
        return None #탐색 실패

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ',end='')
        print()

t = QuadProbing(13)
t.put(25,'grape')
t.put(37,'apple')
t.put(18,'banana')
t.put(55,'cherry')
t.put(22,'mango')
t.put(35,'lime')
t.put(50,'orange')
t.put(63,'watermelon')
print("탐색 결과:")
print('50의 data = ',t.get(50))
print('63의 data = ',t.get(63))
print('해시테이블:')
t.print_table()
    
