s= input("Enter the string : ")
print(''.join(reversed(s)))
print(s[1])
i=0
j=len(s)-1
l=[]
while(j>=0):
    l.append(s[j])
    j-=1
print(''.join(l))