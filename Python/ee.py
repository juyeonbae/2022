#
#G - 7795 먹을 것
"""
T = int(input())
for i in range(T):
    N, M = map(int,input().split()) #N: A의 수, M: B의 수
    A = list(map(int,input().split())) 
    B = list(map(int,input().split()))
    A.sort(reverse = True) #내림차순으로 정리 
    B.sort(reverse = True)
    n = len(A)
    m = len(B)
    tot = 0
    x = 0
    y = 0
    while x < n and y < m: 
        if A[x] > B[y]: #A[x] > B[y] 경우 
            tot += m - y #뒤에 수는 비교할 필요없음(내림차순으로 정렬해서) 
        else:
            y += 1 #A[x] < B[y] 경우 B 리스트 뒤의 수와 비교 
#A 리스트 수 비교 후, 개수 출력 
    print(tot)
"""


#H - 1041 주사위
"""
N = int(input())
a,b,c,d,e,f = map(int,input().split())
"""

#C - 10808 알파벳 (알파벳 소문자만)
"""
word = input()
a_list = [0]*26
#알파벳과 입력값 비교 -> ord() : 숫자로 변환 a=97
for i in word:
    #print(i)
    a_list[ord(i)-97] += 1 #a_list 추가 
for i in a_list:
    print(i, end=' ')
"""

