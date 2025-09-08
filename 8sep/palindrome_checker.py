s=input("Enter the string : ")
s=s.lower()
s1=s.split(" ")
s1=''.join(s1)
if(s1[::]==s1[::-1]):
    print("True")
else:
    print("False")
