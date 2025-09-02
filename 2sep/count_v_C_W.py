s=input("Enter sentence : ")
w=0
c=0
v=0
vow=['a','e','i','o','u']
s1=s.lower()
s2=s1.split(' ')
for i in s2:
    w+=1
    for j in i:
        c+=1
        if(j in vow):
            v+=1
print("Total Words : ",w)
print("Total character : ",c)
print("Total vowels : ",v)