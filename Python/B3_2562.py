#문제설명
"""
최댓값 출력, 최댓값 인덱스 출력
"""

x=[]
for i in range(9):
    n = int(input())
    x.append(n)

print(max(x))
print(x.index(max(x))+1)
"""
x=[]
for i in range(9):
    x.append(map(int,input().split()))
    print(x)
"""
