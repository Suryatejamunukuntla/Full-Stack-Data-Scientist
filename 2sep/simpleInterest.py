p=int(input("Enter pricipal : "))
r=int(input("Enter the rate : "))
t=int(input("Enter the time : "))
it=input("Interest type : ")
if(it.lower()=="simple"):
    total=(p*t*r)/100
    print("Simple Interest : ",total)
    print("Total Amount : ",(total+p))
if(it.lower()=="compound"):
    amount=(p*((1+r/100)**t))
    ci=amount-p
    print("Compound interest : ",ci)
    print("Total amount : ",(ci+p))
