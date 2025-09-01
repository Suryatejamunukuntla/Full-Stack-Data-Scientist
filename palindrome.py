a=input("Enter the name : ")
flag=0
i=0
j=len(a)-1
while(i<j):
    if(a[i]==a[j]):
        i+=1
        j-=1
        flag=1
    else:
        flag=0
        break
if(flag):
    print(a," is a palindrome")
else:
       print(a," is a not palindrome") 