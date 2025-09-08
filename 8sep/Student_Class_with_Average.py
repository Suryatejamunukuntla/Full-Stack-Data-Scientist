class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        s=sum(self.marks)
        l=len(self.marks)
        return s/l
    def add_mark(self,marks):
        self.marks.append(marks)
    def get_highest(self):
        return max(self.marks)
    def get_lowest(self):
        return min(self.marks)
s=Student("Tom", [90, 80, 85])
print("Average marks : ",s.average())   # (90+80+85)/3 = 85.0
s.add_mark(95)           # marks = [90,80,85,95]
print("After adding marks ")
print("Average marks : ",s.average()) 
print("Highest marks : ",s.get_highest())
print("Lowesst marks : ",s.get_lowest())
   # 95
    
        
        