def sort_dict_by_value(d, reverse=False):
    return dict(sorted(d.items(), key=lambda x: x[1], reverse=reverse))


num = int(input("Enter the number of person "))
peps = {}
for _ in range(num):
    name = input("enter the names ")
    amount = int(input("enter the amount "))
    peps[name.title()] = amount
avg = sum(peps.values()) / num
print("average = ", avg)
highest_payer = {k: v - avg for (k, v) in peps.items() if v > avg}
sort_dict_by_value(highest_payer)
print("highest = ", highest_payer)
lowest_payer = {k: v - avg for (k, v) in peps.items() if v < avg}
sort_dict_by_value(lowest_payer)
print("lowest= ", lowest_payer)
for (k, v) in highest_payer.items():
    for (a, b) in lowest_payer.items():
        if v + b > 0:
            print(f"{a} has to pay {-b}rs to {k}")
            if avg + b == 0:
                lowest_payer[a.title()] = 0
                highest_payer[k.title()] = v+b
                print(highest_payer, lowest_payer)
        else:
            print(f"{a} has to pay {v + b}rs to {k}")
    print(highest_payer,lowest_payer)
