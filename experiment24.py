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
counter1=Counter(a)
print(counter1)
counter2=Counter(b)
print(counter2)
print("the difference between 1st list and 2nd list is:",list(counter1-counter2))
print("the difference between 2nd list and 1st list is:",list(counter2-counter1))