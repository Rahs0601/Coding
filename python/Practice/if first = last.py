list = []
n = int(input("enter the array size"))
print("type array elements followed by Enter")
for i in range(0, n):
    x = int(input())
    list.append(x)
print(list)
if list[0] == list[n - 1]:
    print("equal")
else:
    print("not equal")
