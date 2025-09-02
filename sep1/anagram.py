s1=input("Enter the string 1 : ")
s2=input("Enter the string 2 : ")

l1=list(s1)
l2=list(s2)
if(sorted(l1)==sorted(l2)):
    print("both the string are anagram")
else:
    print("not anagrams")