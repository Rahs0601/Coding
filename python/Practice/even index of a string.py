str = input("enter a string\n")
str = str.capitalize()
for i in range(0, len(str) + 1):
    if i % 2 == 0:
        x = str[i]
        x = x.capitalize()
        print("index=", i, x)
        i = i + 1
    else:
        print("")
