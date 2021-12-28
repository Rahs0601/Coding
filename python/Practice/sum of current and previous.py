n= int(input("enter your range"))
print("Printing current and pervois number sum in a range ", n)
for i in range (0,n+1):
    if i==0:
        print( "current number","0" ,   "previous number" ,'0'  , "sum =",  "0")

    else:
        print( "current number",i ,   "previous number" ,i-1  , "sum =",  i+i-1)
    i= i+1