num=int(input("Enter the number : "))
a=0
b=1
for i in range(num):
    print(a,end="  ")
    a,b=b,a+b
    