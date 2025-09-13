try:
    b=int(input("Enter the balance:"))
    w=int(input("enter the withdraw:"))
    if(b>=w):
        print("withdraw amount = ",(b-w))
    else:
        raise Exception("insufficient balance")
except Exception as e:
    print(e)