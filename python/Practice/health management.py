def getdate():
    import datetime
    return datetime.datetime.now()


def write():
    cc = int(input("Please enter client code:\n"
                   "Harry = 1, Rohan = 2, Hammad = 3\n"
                   "Input here: "))
    if cc == 1:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Harry_Food.txt", "a") as HF:
                a = input("Enter food and quantity:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nMeal recorded successfully")
        elif DT == "E":
            with open("Harry_Exercise.txt", "a") as HF:
                a = input("Enter Exercise:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nExercise recorded successfully")
    elif cc == 2:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Rohan_Food.txt", "a") as HF:
                a = input("Enter food and quantity:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nMeal recorded successfully")
        elif DT == "E":
            with open("Rohan_Exercise.txt", "a") as HF:
                a = input("Enter Exercise:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nExercise recorded successfully")
    elif cc == 3:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Hammad_Food.txt", "a") as HF:
                a = input("Enter food and quantity:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nMeal recorded successfully")
        elif DT == "E":
            with open("Hammad_Exercise.txt", "a") as HF:
                a = input("Enter Exercise:\n")
                time = str(getdate())
                HF.write("[" + time + "]" + ":  " + a + "\n")
                print("\nExercise recorded successfully")


def read():
    cc = int(input("Please enter client code:\n"
                   "Harry = 1, Rohan = 2, Hammad = 3\n"
                   "Input here: "))
    if cc == 1:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Harry_Food.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")
        if DT == "E":
            with open("Harry_Exercise.txt") as HF:
                a = HF.read()
                print("\nHere is your exercise log:\n" + a + "\nThanks!!")
    if cc == 2:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Rohan_Food.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")
        if DT == "E":
            with open("Rohan_Exercise.txt") as HF:
                a = HF.read()
                print("\nHere is your exercise log:\n" + a + "\nThanks!!")
    if cc == 3:
        DT = input("Food or Exercise? F/E : ")
        DT = DT.capitalize()
        if DT == "F":
            with open("Hammad_Food.txt") as HF:
                a = HF.read()
                print("\nHere is your food log:\n" + a + "\nThanks!!")
        if DT == "E":
            with open("Hammad_Exercise.txt") as HF:
                a = HF.read()
                print("\nHere is your exercise log:\n" + a + "\nThanks!!")


print("----Welcome to Health Management System----\n")

purp = input("Read old entries or Write new entry? R/W : ")
purp = purp.capitalize()

if purp == "R":
    read()
elif purp == "W":
    write()
