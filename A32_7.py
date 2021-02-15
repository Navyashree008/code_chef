cp = int(input("enter the cost price:-"))
sp = int(input("enter the selling price:-"))
if sp > cp:
    profit = sp - cp
    print("the profit is:-",profit)
elif cp > sp:
    loss = cp - sp
    print("the loss is:-",loss)
else:
    print("no loss no profit")
