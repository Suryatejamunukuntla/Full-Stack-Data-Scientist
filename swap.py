a=int(input("Enter the 1st number : "))
b=int(input("Enter the 2nd number : "))
# a,b=b,a
a=a ^ b
b= a ^ b
a=a^b

print("After the swapping is ",a," ", b)