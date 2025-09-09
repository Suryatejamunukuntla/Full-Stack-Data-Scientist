import os
from collections import Counter
l=[]
#print(os.listdir("C:/TekWorks/python_8sep"))
for i in os.listdir("C:/TekWorks/python_8sep"):
    if(os.path.isfile(i)):
        a,b=os.path.splitext(i)
        l.append(b)
print(dict(Counter(l)))
