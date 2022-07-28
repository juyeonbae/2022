A = int(input())
B = int(input())
C = int(input())

x = list(str(A*B*C))

n = [0,0,0,0,0,0,0,0,0,0]

for i in x:
    n[int(i)] += 1

for i in n:
    print(i)
