#선형조사(Linear Probing)

class LinearProbing:
    def __init__(self,size):    #객체 생성자 
        self.M = size           #테이블 크기 M
        self.a = [None]*size    #해시테이블 a
        self.d = [None]*size    #데이터 저장용 d

    def hash(self,key):
        return key % self.M

    def put(self, key, data):
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 0
        while True:
            if self.a[i] == None:       #빈 곳 발견 
                self.a[i] = key         #key는 해시테이블에 
                self.d[i] = data        #data는 리스트 d에 저장 
                return
            if self.a[i]==key:
                self.d[i] = data  #key가 이미 해시테이블에 있음/data만 갱신
                return
            j += 1
            i = (initial_position + j)%self.M
            if i == initial_position:
                break  #다음 위치가 초기 위치와 같으면 루프 벗어나기(저장 실패)

    def get(self,key):
        initial_position = self.hash(key) #초기 위치 
        i = initial_position
        j = 1
        while self.a[i] != None:
            if self.a[i] == key:
                return self.d[i]    #탐색 성공 
            i = (initial_position + j) % self.M #다음 원소 검사를 위해 
            j += 1
            if i == initial_position:
                return None             #탐색 실패 
        return None

    def print_table(self):
        for i in range(self.M):
            print('{:4}'.format(str(i)),' ',end='')
        print()
        for i in range(self.M):
            print('{:4}'.format(str(self.a[i])),' ',end='')
        print()

t = LinearProbing(13)
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
