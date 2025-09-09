l=eval(input("Enter the list :"))
c1=0
c2=0
c3=0
for i in l:
    if(i==0):
        c1+=1
    if(i<0):
        c2+=1
    if(i>0):
        c3+=1

print("Postive=",c3,"Negetive=",c2,"zeros=",c1)
