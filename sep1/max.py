a=eval(input("Enter the points"))
res=a[0]
for i in a:
    if(res<i):
        res=i
print("highest is ",res)
