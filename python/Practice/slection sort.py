def sort(list):
    for i in range(5):
        min = i
        for j in range (i,6):
            if list[j]<list[min]:
                min =j
        list[i],list[min]=list[min],list[i]


list =[8,6,2,5,9,4]
sort(list)
print(list)