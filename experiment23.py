a=list()
n=int(input('enter how many numbers:'))
for i in range(n):
    b=input('enter character:')
    a.append(b)
print(a)
c=int(input('enter the spliting point:'))
for i in range(c):
    print(a[i::c])