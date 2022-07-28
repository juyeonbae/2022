a = [1,1,1,1,2,2,2,3,3,4]

c1 = a.count(1)
c2 = a.count(2)
c3 = a.count(3)
c4 = a.count(4)

k = int(input())

while k>=0:
    if c1>=k:
        print(1)
        if c2>=k:
            print(2)
            if c3>=k:
                print(3)
                if c4>=k:
                    print(4)
    else:
        break
    break

from collections import Counter
list = [1,1,1,2,2,3]
result = Counter(list)
for key in result:
    print(key,result[key])

#k번이상 X
    
