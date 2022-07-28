#1단원 연습문제

#1.22
def abc(n):
    r=n%2
    print('*',end='')
    if n>=2:
        abc(n//2)           #abc(2) abc(4) abc(9) ~~ 안에 있는 함수부터 출력됨 
    print('%d' %r, end='')
    return
  
abc(78)
print('\n')

#1.23
def test(s, last):
    if last<0:
        return 0
    if s[-1] =='0':
        return 2*test(s,last-1)
    return 1+2*test(s,last-1)

test('110100111',4)


return 1+2*test(110100111,3) 1+2*7 => 15
return 1+2*test(110100111,2) 1+2*3 => 7
return 1+2*test(110100111,1) 1+2*1 => 3
return 1+2*test(110100111,0) 1+2*0 => 1
return 1+2*test(110100111,-1) => 0
