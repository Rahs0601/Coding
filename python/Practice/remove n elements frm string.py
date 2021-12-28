x = input("enter the string\n")
y = int(input("enter how many numbers to remvoe\n"))
def remove(x,y):
    for i in range (0, len(x)):
        if i>=y:
            print(x[i],end="")
if len(x)<y:
    print("invalid ,nothing left ")
elif len(x)==y:
    print("evrything removed")
else :
    remove(x,y)