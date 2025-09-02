pin=int(input("Enter the pin : "))
bal=int(input("Enter the balance : "))
wd=int(input("Enter the withdraw amount : "))
if(pin==1234):

    print("pin verfied")
    if(bal>=wd):

        print("Withdrawal Successful. Remaining Balance = ",(bal-wd))
    else:
        print("Insufficient Balance")
else: 
    print("pin not verfied")