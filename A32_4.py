num1 = int(input("enter number"))
num2 = int(input("enter number"))
num3 = int(input("enter number"))
if num1 > num2:
    if num1 < num3:
        print(num1,"is second max")
elif num1 > num3:
    if num1 < num2:
        print(num1,"is second max")
elif num2 > num1:
    if num2 < num3:
        print(num2,"is second max")
elif num2 > num3:
    if num2 < num1:
        print(num2,"is second max")
else:
    print(num3,"is second max")

