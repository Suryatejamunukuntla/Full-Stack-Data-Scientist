a, b, c, d, e = map(int, input("Enter five numbers separated by space: ").split())
sum=a+b+c+d+e
percent=(sum/500)*100
if(percent>=90):
    print("A")
elif(percent>=75 and percent<90):
    print("B")
elif(percent>=50 and percent<75):
    print("C")
else:
    print("Fail")
