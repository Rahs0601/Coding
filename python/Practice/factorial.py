# without recursion
def fact(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f


x = int(input("enter a number u want to find factorial of "))
result = fact(x)
print(result)


# with recursion
def facto(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * facto(n - 1)


fc = facto(x)
print(fc)
