l=[]
n=int(input('enter size of list:'))
for i in range(n):
    c=input("enter elements:")
    l.append(c)
print("the list with duplicates is:",l)
t1=tuple(dict.fromkeys(l))
print("the tuplle without duplicates is:",t1)
