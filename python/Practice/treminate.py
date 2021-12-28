#no matter what sequence of list u enter in binary its gonna terminate
#facedown =1 , f11aceup =0
a = list("010100110100101")
print(a)
b = a.copy()


def tranform(x):
    for i in range(len(x)-1):
        if x[i]=='1':
            x[i]= '0'
            if x[i+1]=='1':
                x[i+1]=='0'
               
            else:
                x[i+1]==1
            
    return x
b = tranform(b)
print(b)