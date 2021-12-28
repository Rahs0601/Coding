list = [81,53,90,73,91]
n=  len(list)
def sort(list):
    for j in range(n-1):
        for i in range(0, n-j-1):
            if list[i]>list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
               
                

sort(list)
print(list)

 





