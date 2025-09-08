a=int(input("Enter the number : "))
b=str(a)
l=len(b)-1
i=a
sum=0
while(i!=0):
    i=i%10
    sum=i**l
    i=i//10
if(i==sum):
    print(a,"Is armstrong")
else:
    print(a,"is not armstrong")
