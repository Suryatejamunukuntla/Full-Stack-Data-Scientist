d=eval(input("Enter the data : "))
s=input("search : ")
for i in d:
    if(i.lower()==s.lower()):
        print("phone number of ",i, " is" , d.get(i))