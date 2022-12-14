#문제 설명
"""
1. 금메달 수가 더 많은 나라
2. 금메달 수가 같으면 은메달 수가 더 많은 나라
3. 금, 은메달 수가 모두 같으면, 동메달 수가 더 많은 나라

한 국가의 등수는 (자신보다 더 잘한 나라 수) + 1로 정의

입력
국가의 수 N, 등수를 알고 싶은 국가 K가 빈칸을 사이에 두고-> N, K = map(int,input().split())
이후 N개의 각 줄에는 차례대로 각 국가를 나타내는 정수(국가 이름 표시 = 숫자)
-> for i in range(N):
    x = list(map(int,sys.stdin.readline().split()))
        x[0] = 국가 구분/x[1] = 금/x[2] = 은/x[3] = 동
=> 람다 함수로 정렬 조건 정해주기 
"""

import sys
N, K = map(int, input().split())
x=[]
for i in range(N):
    x.append(list(map(int,sys.stdin.readline().split())))
x.sort(key=lambda x:(-x[1],-x[2],-x[3]))
#lambda함수 x리스트를 x[1], x[2], x[3] 순으로 오름차순 정렬/-붙이면 내림차순 정렬

for i in range(N):
    if x[i][0] == K:
        index = i
for i in range(N):
    if x[index][1:] == x[i][1:]:
        
        print(i+1)
        break
    
#x[][1:] = x[1] 번째 포함한 이후 나머지 배열
#어렵거나 헷갈리는 부분
#1. lambda 함수로 정렬 설정하는 게 헷갈림 -> 해결  
#2. 메달이 같을 때 순위 결정하는 방법 어려움 -> 2차원 배열로         
