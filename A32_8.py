roll_no = int(input("enter the roll number"))
if  roll_no > 0:
    if roll_no % 5 == 0:
        print("leader of the group")
    else:
        print("not a leader")
else:
    print("check the input again")