s=input("Enter the password to check : ")
u=False
l=False
d=False
sp=False
for i in s:
    if(i.isalpha):
        if(i.islower()):
            l=True
        if(i.isupper()):
            u=True
    if(i.isdigit()):
        d=True
    if(not i.isalnum):
        sp=True
if(len(s)>=8 and l and u and d and sp):
    print("Strong Password")
else:
    print("Weak Password")