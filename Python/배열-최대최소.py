level = list(map(int,input().split()))  #난이도별 점수 저장 리스트 
n = int(input())                        #참가 동아리 수 입력
grades = []                             #동아리 점수 저장 리스트 
for i in range(n):                      #동아리가 얻은 점수 구함 
    grade = 0                           #초기화 
    for j in range(3):                  #부원 3명 -> a로 리스트 입력 받음 
        a = list(map(int, input().split()))
        for k in range(3):              #부원 당 점수 계산 
            grade += a[k] * level[k]
        grades.append(grade)            #리스트에 삽입 

print(max(grades))                     #grades리스트에서 최댓값 출력 
