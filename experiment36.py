class rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        print("the area of rectangle is:",self.length*self.width)
 
l=int(input("enter length of rectangle:"))
w=int(input("enter width of rectangle:"))
v=rectangle(l,w)
v.area()