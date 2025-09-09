print("Welcome to calculator")
while(True):
    print("Addition(1)\nsubtraction(2)\nproduct(3)\ndivision(4)\nexit(5)")
    print("Enter your choice : ")
    c=int(input())
    if(c==1):
        print("Enter the a value")
        a=int(input())
        print("Enter the b value")
        b=int(input())
        print("Addition of ",a," ",b," ",(a+b))
        print()
    if(c==2):
        print("Enter the a value")
        a=int(input())
        print("Enter the b value")
        b=int(input())
        print("sub of ",a," ",b," ",(a-b))
        print()
    elif(c==3):
        print("Enter the a value")
        a=int(input())
        print("Enter the b value")
        b=int(input())
        print("Product of ",a,"+",b,"=",(a*b))
        print()
    elif(c==4):
        print("Enter the a value")
        a=int(input())
        print("Enter the b value")
        b=int(input())
        print("Addition of ",a," ",b," ",(a/b))
        print()
    elif(c==5):
        exit(0)
    else:
        print("invalid , try again")
