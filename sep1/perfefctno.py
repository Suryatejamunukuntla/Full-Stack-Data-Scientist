num=int(input("Enter the number : "))
sum=0
for i in range(1,num):
    if(num%i==0):
        sum+=i
if(sum==num):
    print(num," is the perfect number")
else:
    print(num," is the not a perfect number")
