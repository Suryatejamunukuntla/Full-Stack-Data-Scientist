d={}
sum=0
n=int(input("enter the no. of items : "))
for i in range(n):
    a,b=list(map(str,input("Enter the name and price with , seperated ").split(",")))
    d[a]=b
print("defaulter are :")
for i in d.keys():
    sum+=float(d[i])
print(f"Total bill is {sum:.2f}")