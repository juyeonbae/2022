def gugudan(dan):
    for i in range(1,10):
        print(dan, "*", i, "=",dan*i)

def inputDan():
    dan = int(input())
    gugudan(dan)
    
inputDan()
