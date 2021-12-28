def add(a,b):
        return a+b
def sub(a,b):
        return a-b
def mul(a,b):
        return a*b
def div(a,b):
        return a/b
print ('select opertion')
print ('1. add')
print ('2. sub')
print ('3. mul')
print ('4. div')

while True:
    choice = int(input("ur choice=\n "))
    a = int(input('enter first number\n'))
    b = int(input('enter 2nd number\n'))
    if choice == 1:
        result = add(a,b)
        print(result)
    elif choice ==2:
        result = sub(a,b)
        print(result)
    elif choice == 3:
        result = mul(a,b)
        print(result)
    elif choice ==4:
        if b==0:
            print("zero divison invalid")
        else:
            result = div(a,b)
            print(result)
    else:
        print("Enter vaild choice ")
    break 