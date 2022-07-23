import cmath
a=int(input("enter x**2 coefficient:"))
b=int(input("enter x cofficient:"))
c=int(input("enetr constant"))
d=(b**2)-(4*a*c)
sol1=(-b-cmath.sqrt(d))/(2*a)
sol2=(-b+cmath.sqrt(d))/(2*a)
print("the square roots are:",sol1,sol2)