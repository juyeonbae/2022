#10866

import sys
from collections import deque 

N = int(input())
dq = deque()

for i in range(N):
    x = list(sys.stdin.readline().split())

    if x[0] == "push_front":
        dq.appendleft(x[1])     
        
    elif x[0] == "push_back":
        dq.append(x[1])         
        
    elif x[0] == "pop_front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
            
    elif x[0] == "pop_back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
            
    elif x[0] == "size":
        print(len(dq))
        
    elif x[0] == "empty":
        if len(dq) == 0: print(1)
        else:
            print(0)
            
    elif x[0] == "front":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
            
    elif x[0] == "back":
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])



"""
python deque 사용법

1. collections 모듈 및 deque import
- from collections import deque
2. deque 생성
- dq = deque()/print(dq) -> print 결과 : deque([])
3. append() : deque 뒤(오른쪽)에 값 추가
- dq.append(5)/dq.append(6)/print(dq) -> deque([5,6])
4. appendleft() : deque 앞(왼쪽)에 값 추가
- dq.appendleft(4)/ dq.appendleft(3)/print(dq) -> deque([3,4,5,6])
5.extend() : deque 뒤(오른쪽)에 iterable 객체를 순환하며 값들을 차례로 추가
- dq.extend([7,8,9])/print(dq) -> deque([3,4,5,6,7,8,9])
6. extendleft() : deque 앞(왼쪽)에 iterable 객체를 순환하며 값들을 차례로 추가
(객체의 마지막 값부터 deque에 추가됨)
- dq.extendleft([2,1,0])/print(dq) -> deque([0,1,2,3,4,5,6,7,8,9])
7. remove() : deque 안의 특정 값 삭제
- dq.remove(7)
8. pop() : deque 뒤(오른쪽)의 값 삭제 후 반환
- popValue = dp.pop()/print(popValue)->6 / print(dq) -> deque([0,1,2,3,4,5])
9. popleft() : deque 앞(왼쪽)의 값 삭제 후 반환
- popValue = dq.popleft()/print(popValue)-> 0 /print(dq)->deque([1,2,3,4,5])
10. rotate() : deque 안의 값들 회전
- print(dq) -> deque([1,2,3,4,5])
- dq.rotate(1)
- print(dq) -> deque([5,1,2,3,4])
- dq.rotate(-1)
- print(dq) -> deque([2,3,4,5,1])
"""
