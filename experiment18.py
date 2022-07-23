def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
n=int(input('enter a value:'))
if n<0:
    print("factorial is not posssible for negative numbers")
elif n==0:
    print("the factorial is 0 is:1")
else:
    print("factorail of",n,"is:",factorial(n))
    