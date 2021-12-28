sum = 0
while True:
    a = input("enter the price of item or press q to exit\n ")
    if a != 'q':
        a = int(a)
        sum = sum + a
        print(f" oder total so far:{sum}\n ")
    else:
        print(f"your total is {sum}", " \n Thanks for shopping ")
        break
