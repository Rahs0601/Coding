n = 56
left = 1
while (left <= 5):
    m = int(input("enter your number\n"))
    if m > n:
        print("lesser ur guess\n")
    elif m == n:
        print("you own\n")
        break
    else:
        print("increase the guessed number\n")
    print(5 - left, "number of guesses left")
    left = left + 1
if left > 5:
    print("game over")
