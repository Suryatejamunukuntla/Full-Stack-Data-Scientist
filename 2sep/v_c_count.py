s=input("Enter the string : ")
v=['a','e','i','o','u']
tl=len(s)
s1=s.lower()
vc=0

for i in s:
    if( i in v):
        vc+=1
print("vowels are ",vc)
print("consonents are ",tl-vc)

