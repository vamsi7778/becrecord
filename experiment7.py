n=int(input("enter an integer"))
print("the divisors of the given number are")
for i in range(1,n+1):
    if(n%i==0):
        print(i)