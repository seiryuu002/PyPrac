class Line:
    
    def __init__(self, coordinate_1, coordinate_2):
        self.x1, self.y1 = coordinate_1
        self.x2, self.y2 = coordinate_2
    
    def distance(self):
        return ((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)**0.5
    
    def slope(self):
        return (self.y2 - self.y1)/(self.x2 - self.x1)

class Cylinder:

    pi = 3.14
    def __init__(self, radius = 1, height = 1):
        self.radius = radius
        self.height = height
    
    def volume(self):
        return (self.radius*self.radius*self.height)*Cylinder.pi
    
    def surface_area(self):
        return (2*Cylinder.pi*self.radius*self.radius)+(2*Cylinder.pi*self.radius*self.height)


cor1 = (3,2)
cor2 = (8,10)
print('\n'*2)
line = Line(cor1,cor2)
print(line.distance())
print(line.slope())

cylinder = Cylinder(3,2)
print(cylinder.volume())
print(cylinder.surface_area())

