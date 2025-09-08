s=input("Enter sentence : ")
c=0
v=0
vow=['a','e','i','o','u']
s1=s.lower()
s2=s1.split(' ')
for i in s2:
    for j in i:
        c+=1
        if(j in vow):
            v+=1
print("Vowels = ",v,", Consonants = " ,c-v)
