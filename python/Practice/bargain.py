# if bargain price is more than 91% of mrp give it
# if it less then 52% of mrp than throw him out of the shop
# if it in between try convincing to take for more than 91%

MRP = float(input("Enter the MRP\n"))
a = (MRP * 52) / 100
b = (MRP * 91) / 100
while True:
    Bargain = float(input("enter bargain amount\n"))
    if MRP >= Bargain >= b:

        print(f"you can take this product for {Bargain} ₹\n")
        break
    elif Bargain <= a:
        print(Bargain, "₹ amount is less you can try again for more")
    elif Bargain > MRP:
        print(f'{Bargain} is higher than {MRP}')
    else:
        print("At that price even raw material won't come sorry!!!")
        print("next time come with more money lol")
        break
if Bargain >= b:
    print("Thanks for coming, Visit again , Have a nyc day!")
