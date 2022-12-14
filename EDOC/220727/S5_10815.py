#10815 숫자 카드
"""
문제 설명
숫자 카드는 정수 하나가 적혀져 있는 카드이고, N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 갖고 있는지 아닌지
구하는 프로그램
입력
첫째 줄에는 갖고 있는 숫자 카드의 개수 N개가 주어짐.(1<=N<=500,000)
둘째 줄에는 숫자 카드에 적혀있는 정수가 주어진다.(-10,000,000<=수<=10,000,000)
*두 숫자 카드에 같은 수가 적혀있는 경우는 없다.
셋째 줄에는 M이 주어진다. (1<=M<=500,000)
넷째 줄에는 갖고 있는 숫자 카드인지 아닌지를 구해야 할 M개의 정수가 주어지며,
이 수는 공백으로 구분되어져 있다. (-10,000,000<=수<=10,000,000)
출력
첫째 줄에 입력으로 주어진 M개의 수에 대해서,
각 수가 적힌 숫자 카드를 갖고 있으면 1, 아니면 0을 공백으로 구분해 출력
"""
import sys

N = int(input()) 
num = list(map(int,sys.stdin.readline().split()))
M = int(input())
check = list(map(int,sys.stdin.readline().split()))

num.sort()      #이진탐색 하기 위해 정렬

def bin_search(a,key,left,right):
    while start<=end:
        mid = (left+right)//2
        if a[mid] == key:
            return mid
        elif a[mid]>key:
            right = mid -1
        else:
            left = mid +1
    return None

for i in range(M):
    if bin_search(num,check[i],0,N-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')
    
#시간복잡도 줄이기 -> set(집합함수) 자료구조 hash 사용 

import sys

N = int(input())
card = set(map(int,sys.stdin.readline().split()))
M = int(input())
check = list(map(int,sys.stdin.readline().split()))

for i in check:
    if i in card:
        print(1,end=' ')
    else:
        print(0,end=' ')
