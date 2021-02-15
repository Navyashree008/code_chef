num = int(input("enter number"))
if num % 2 == 0:
    if num > 200:
        print("bingo")
elif num % 2 == 1:
    if num < 200:
        print("ringo")
else:
    print("code chef")