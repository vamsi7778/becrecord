class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        print("the area of circle is:",self.radius**2*3.14)
    def perimeter(self):
        print("the perimeter of circle is:",2*self.radius*3.14)
r=int(input("enter the radius of the circle:"))
v=circle(r)
v.area()
v.perimeter()