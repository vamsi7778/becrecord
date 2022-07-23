from collections import Counter
l=[]
n=int(input("enter the size of tupple:"))
for i in range(n):
    c=input("enter elements:")
    l.append(c)
t=tuple(l)
c=Counter(t)
print('the tuple is:',t)
t1=tuple(dict.fromkeys(t))
c1=Counter(t1)
print("the repeated elements in the tuple are:",tuple(dict.fromkeys(c-c1)))
