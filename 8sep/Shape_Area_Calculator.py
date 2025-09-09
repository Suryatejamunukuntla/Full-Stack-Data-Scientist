import math
class shape:
    def __init__(self,name):
        self.name=name
    def area(self):
        raise NotImplementedError
    
class Circle(shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius=radius
    def area(self):
        return math.pi*self.radius*self.radius
    
class Rectangle(shape):
    def __init__(self, width,height):
        super().__init__("Restangle")
        self.width=width
        self.height=height
    def area(self):
        return self.height*self.width
c=Circle(7)
print(f"Area of circle (7) is {c.area():.2f}")
r=Rectangle(4,5)
print("area of rectangle (4x5) ",r.area())

    
        
        