price1 = int(input("enter first price:-"))
price2 = int(input("enter second price:-"))
price3 = int(input("enter third price:-"))
if price1 > price2:
    if price1 > price3:
        print("highest price is",price1)
elif price2 > price3:
    if price2 > price1:
        print("highest price is",price2)
else:
    print("highest price is",price3)