x = int(input('enter a nuber'))

def fib(x):
    a=0
    b=1
    if (x<=0):
        print("invalid, number should be positive and grater then zero")
    elif (x==1):
        print(a)
    elif(x==2):
        print(a)
        print(b)
    else:
        print(a)
        print(b)
        for i in range(2,x):
            c = a+b
            a=b
            b=c
            print(c)
fib(x)


def fib0(x):
    if x == 0:
        return 0
    elif x ==1 or x ==2:
        return 1
    else:
        return fib0(x-1)+fib0(x-2) 
d = fib0(x)
print("sum is", d )