try:
    a=int(input("enter the number1 : "))
    b=int(input("enter the number2 : "))
    print("division is ",(a/b))
except(ValueError):
    print("value Error type input")
except(ZeroDivisionError):
    print("number cant be divided by 0")
except:
    print("zero division error")