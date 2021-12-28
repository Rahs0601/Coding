def fact(number):
    if number < 0:
        print("invalid")
        return
    elif number == 0:
        return 1
    return number * fact(number - 1)


x = int(input("enter a number\n"))
result = fact(x)

print(result)
