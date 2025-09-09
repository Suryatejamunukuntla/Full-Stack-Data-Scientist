d={}
n=int(input("enter the no. of student : "))
for i in range(n):
    a,b=list(map(str,input("Enter the name and percent with , seperated ").split(",")))
    d[a]=b
print("defaulter are :")
for i in d.keys():
    if(int(d[i])<75):
        print(i)