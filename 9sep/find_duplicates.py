l=eval(input("Enter the students list : "))
d={}
for i in l:
    d[i]=l.count(i)
print("duplicates : ")
for i in d.keys():
    if(d[i]>1):
        print(i,end=" ")
    