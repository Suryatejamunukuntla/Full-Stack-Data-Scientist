marks=eval(input("Enter the marks in list form : "))
s=sum(marks)
avg=s/len(marks)
if(avg>=80):
    print("Grade A")
elif(avg>=60 and avg<80):
    print("Grade B")
elif(avg>=40 and avg<60):
    print("Grade C")
else:
    print("Fail")
