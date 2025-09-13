import os
# sum=0
# with open("text.txt","r") as f:
#     for i in f.read():
#         s=i.split("")
#         sum+=len(s)
# print("Total words : ",sum)
    

word_count = 0
with open("text.txt", "r") as f:
    for line in f:
        words = line.split()  # Splits on any whitespace
        word_count += len(words)

print("Total words:", word_count)

