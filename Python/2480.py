#2480 6/29

a,b,c = map(int,input().split()) 

if a==b or a==c or b==c:
    if (b==c and a==c) or (a==b and b==c) or (a==b and a==c):
        print(10000+a*1000)
    else:
        if a==b or a==c:
            print(1000+a*100)
        elif b==c:
            print(1000+b*100)
else:
    if a>b:
        if a>c:
            print(a*100)
        else:
            print(c*100)
    else:
        if b<c:
            print(c*100)
        else:
            print(b*100)
