# shop for "" in INR and get flat
# min shop should be 100 ₹
# 100 and get 1% off
# 500 and get 5% off
# 1000 and get 10% off
# 5000 and get 50% off


sum = 0
Total_bill = 0
while True:
    a = input("enter the price of item or press q to exit\n ")
    if a != 'q':
        a = int(a)
        sum = sum + a
    else:
        break
if sum >= 5000:
    print(f'congratulations you got 50%  discount , your order is of {sum}₹')
    Total_bill = sum - (sum * 50) / 100
elif sum >= 100:
    print(f'congratulations you got 10%  discount , your order is of {sum}₹')
    Total_bill = sum - (sum * 10) / 100
elif sum >= 500:
    print(f'congratulations you got 5%  discount , your order is of {sum}₹')
    Total_bill = sum - (sum * 5) / 100
elif sum >= 100:
    Total_bill = sum - (sum * 1) / 100
    print(f'congratulations you got 2%  discount , your order is of {sum}₹ ')
print("YOUR TOTAL BILL IS:", int(Total_bill) + 1, "₹")
