x = int(input('enter a number\n'))


def fib(number):
    a = 0
    b = 1
    if number < 0:
        print("invalid, number should be positive and grater then zero")
    elif number == 0:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2, number):
            c = a + b
            a = b
            b = c
            if c <= number:
                print(c)


fib(x)
