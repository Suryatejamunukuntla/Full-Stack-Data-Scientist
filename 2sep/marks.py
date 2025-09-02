a=eval(input("Enter the marks : "))
m=max(a)
mi=min(a)
sum=0
for i in a:
    sum+=i
print("maximum = ",m)
print("Mainimum = ",mi)
print("Average = ",(sum/len(a)))