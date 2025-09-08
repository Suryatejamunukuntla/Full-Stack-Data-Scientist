s=input("Enter the string : ")
l=s.split(" ")
li=[]
for i in range(len(l)):
    li.append(len(l[i]))
m=max(li)
index=li.index(m)
print(l[index])
