l=[]
n=int(input("enter size of tuple:"))
for i in range(n):
    c=input("enter elements:")
    l.append(c)
t=tuple(l)
print("the tuple is :",t)
r=t[::-1]
print("the tuple after reversing tuple is:",r)