a=list()
n=int(input('enter how many numbers:'))
for i in range(n):
    b=input('enter characters:')
    a.append(b)
print(a)
n1=int(input('enter  a number:'))
print("output is:")
l=['{}{}'.format(x,y+1) for y in range(n1) for x in a]
print(l)
    