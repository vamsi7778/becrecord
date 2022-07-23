from collections import Counter
a=list()
b=list()
n=int(input('enter size of 1st list:'))
for i in range(n):
    c=input("enter strings:")
    a.append(c)
n1=int(input('enter size of 2nd list:'))
for i in range(n1):
    c=input("enter strings:")
    b.append(c)
print("the 2nd list is:",b)
a[-1]=b
print("the resultant list is:",a)