
m = int(input("enter the number of rows\n"))
for i in range(m+1):
        for j in range(i):
            print(i,end="")
            
        print('\n')
for i in range(m+1,1,-1):
        for j in range(i):
            print("*",end="")
        print('\n')
for i in range(m+1):
    for j in range(i):
        print(j+1 , '', end= "")
    print()
for i in range(5):
    if i ==0:
        for j in range(2):
            print('$', end="")
    elif i==3:
        for j in range(4):
            print('$', end="")
    else:
        print("$","","$")