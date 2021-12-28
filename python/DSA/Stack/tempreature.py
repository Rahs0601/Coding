def printNGE(arr):
    next =[]
    for i in range(0,len(arr),1):
        for j in range(i+1, len(arr),1):
            if arr[i]<arr[j]:
                next.append(j-i)
                break
        if arr[i]>arr[j]:
            next.append(0)
            break
    next.append(0)
    print(next)
temperatures = [30,60,90]
printNGE( temperatures )