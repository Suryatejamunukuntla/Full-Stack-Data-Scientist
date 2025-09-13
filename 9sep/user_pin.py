pin=1234
attempts=3
while (attempts>0):
    n=int(input("enter the pin : "))
    if(n==1234):
        print("pin matched")
        break
    print("Try again")
    attempts-=1

    