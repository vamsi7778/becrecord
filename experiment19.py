f2=open("file19.txt",'w')
f2.write("vamsi is a good boy in andhra")
f2.close()
f1=open("file19.txt",'r')
t=f1.readlines()
for i in t:
    max=' '
    for j in i.split():
        if(len(j)>len(max)):
            max=j
print(max)