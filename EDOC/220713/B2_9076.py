#문제 설명
"""
입력: 여러 줄을 입력 받으므로 sys.stdin.readline 사용
+)한 줄에 점수 5개를 받으므로 끊어서 입력값을 받는 map 함수 사용 
최고점과 최저점을 뺀 나머지 3명 점수
-> 리스트에 입력값 저장 후 오름차순으로 정렬/나머지 3명 점수 = x[1]~x[3]이 됨
나머지 3명 점수의 최고점과 최저점의 차이가 4점 이상 나게 되면 KIN 출력
-> x[3]-x[1]>=4일 경우 KIN 출력/조건문 사용
-> else: x[1]+x[2]+x[3] 
"""

import sys

T = int(input())
for i in range(T):
    x = list(map(int,sys.stdin.readline().split()))
    #임의의 개수의 정수를 한줄에 입력받아 리스트에 저장할 때
    x.sort()
    if x[3]-x[1]>=4:
        print("KIN")
    else:
        print(x[1]+x[2]+x[3])

#input() 대신 sys.stdin.readline 쓰는 이유
#반복문으로 여러줄을 입력 받아야 할 때 시간초과가 발생할 수 있기 때문 

#어렵거나 헷갈린 점 - 딱히 없음 
