num = int(input("enter number"))
if num > 0:
    if num % 5 == 0 and num % 11 == 0:
        print("both")
    elif num % 5 == 0:
        print(5)
    elif num % 11 == 0:
        print(11)
    else:
        print("none")    

