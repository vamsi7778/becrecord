a=input("enter any body:")
b=a.upper()
c=input("enter any head:")
def f(b,c):
    print('<{}>{}</{}>'.format(c,b,c))
f(b,c)