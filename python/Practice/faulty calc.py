# faulty calculator
# 45*3 =555, 56+9 =7, 56/6 =4
def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


print('select operation')
print('1. add')
print('2. sub')
print('3. mul')
print('4. div')

while True:
    choice = int(input("ur choice=\n "))
    a = int(input('enter first number\n'))
    b = int(input('enter 2nd number\n'))
    if choice == 1:
        if a == 56 and b == 9:
            result = 7
        else:
            result = add(a, b)
        print(result)
    elif choice == 2:
        result = sub(a, b)
        print(result)
    elif choice == 3:
        if a == 45 and b == 3:
            result = 555
        else:
            result = mul(a, b)
        print(result)
    elif choice == 4:
        if a == 56 and b == 6:
            result = 4
        elif b == 0:
            print("zero division invalid")
        else:
            result = div(a, b)
            print(result)
    else:
        print("invalid")
    break
