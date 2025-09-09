class Manager:
    def __init__(self,name,salary,role):
        self.name=name 
        self.salary=salary
        self.role=role
    def bonus(self):
        if(self.role=="Manager"):
            return int(self.salary*0.2)
        if(self.role=="Developer"):
            return self.salary*0.1
        if(self.role=="Intern"):
            return int(self.salary*0.05)
m=Manager("Alice",50000,"Manager")
print(m.bonus())



