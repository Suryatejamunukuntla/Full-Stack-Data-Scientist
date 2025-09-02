a=input("Enter the string")
cu=0
cl=0
for i in a:
    if(i.isupper()):
        cu+=1
    if(i.islower()):
        cl+=1
print("The upper case are ",cu)
print("the lower case are ",cl)