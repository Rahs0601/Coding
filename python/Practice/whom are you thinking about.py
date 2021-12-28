print("Hey There whats your good name")
name = input()
print(f"nice to meet you {name}")
gender = input("your gender M\F \n")
print("whats your age ")
age = int(input())
if age > 50 and gender == 'M':
    print("yes my old man")
    print("take rest before you rest in peace")
elif age <= 18 and gender =="M":
    print("ABE padai likai karo IAS YAS Bano !!")
elif gender == "M":
    while (True):
        print("think of any charcter you want \n")
        ans = input("type y to contine or q to quit\n")
        if ans == "q":
            print("Bosdike karne kya aethe\n")
            break
        else:
            print("Is your charcter female?")
            ans = input('y or n')
            if ans == "y":
                print("sirf ladikya hi hai thumare dimak mai bosdi wale")
            else:ans = input("type y to contine or q to quit\n")
            print("madarchod thu mard nahi hai kya?")
else :
    print("hey beautiful lets start the game")
    ans = input("type y to contine or q to quit\n")
    print("think of any charcter you want")
    while (True):
        if ans == "q":
            print("Thanks for coming ma'am have a nyc day")
            break
        else:
            ans = input("type y to contine or q to quit")
            print("Is your charcter female?")
            ans = input('y or n')
            if ans == "y":
                print("Is your charter frm k-pop girl gang")
                ans = input('y or n')
                if ans== "y":
                    print("I dont know there names sorry")
                    print("you can restart the game ")
            else:
                print('Is your charter frm k-pop/k-drama gang')
                ans = input('y or n')
                if ans == "y":
                        print("I dont know there names sorry")
                        print("you can restart the game ")
                else:
                    print("Is your charcter from any movie")
                    ans = input('y or n')
                    if ans == "y":
                            print("Be realistic ma'am")
                    else:
                        print("does he know you ")
                        ans = input('y or n')
                        if ans == "y":
                            print("does he love you")
                            ans = input('y or n')
                            if ans == "y":
                                print("easy your boyfriend")
                            else:
                                print("may be a gud friend of yours")