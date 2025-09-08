import time
s=input()
i1=s.index("(")+1
i2=s.index(")")
s2=s[i1:i2]
num=eval(s2)
i=num
while(i>0):
    print(i)
    time.sleep(1)
    i-=1
print("Time's up!")
