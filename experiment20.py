    f1=open("file3.txt","r")
t=f1.readlines()
print("the content is:",t)
f2=open("file4.txt","r")
t1=f2.readlines()
print("the content is:",t1)
for i,j in zip(t,t1):
	print((i+j).replace("\n"," "))
	