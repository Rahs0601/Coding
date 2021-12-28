#if bill < 50 charge 50
#if bill < 100 charge 100
#if bill <200 chrage 200
#if bill <500 chrage 500
#for bill > 1000 charge same amount 


sum = 0
while True:
    a = input("enter the price of item or press q to exit\n ")
    if  a!='q':
        a = int(a)
        sum = sum + a
    else:
        break
if sum<50:
    sum= 50
elif sum < 100:
    sum = 100
elif sum < 200:
    sum = 200
elif sum < 500:
    sum = 500
else:
    sum = sum
print (f" your bill is {sum}")
