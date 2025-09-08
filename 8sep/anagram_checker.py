s1,s2=map(str,input("Enter the Strings : ").split(","))

l1=list(s1)
l2=list(s2)
if(sorted(l1)==sorted(l2)):
    print("True")
else:
    print("False")