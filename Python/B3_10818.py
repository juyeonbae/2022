#문제 설명
"""
N개의 정수의 최솟값과 최댓값을 구하는 프로그램
"""

n = int(input())
x = list(map(int,input().split()))
print(min(x),max(x))

