alp=input("enter a string:")
total=0
vowel=0
for i in alp:
    total=total+11
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U':
        vowel=vowel+1
print("no of vowels are:")
print(vowel)
percentage=vowel/total*100
print("vowel percentage in string is:")
print(percentage)