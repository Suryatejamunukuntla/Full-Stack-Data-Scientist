n=int(input("Enter the units : "))
if(n<=100):
    print("Bill is ",(n*5))
elif(n<=200 and n>100):
    sum=100*5
    sum+=(n-100)*7
    print("Bill is ",sum)
else:
    sum=100*5
    sum+=100*7
    sum+=(n-200)*10
    print("Bill is ",sum)
