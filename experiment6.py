string="Chandigarh University"
print(string)
print(string[0]+string[-10])
print(string[-1])
s1=string[2:16:2]
s2=string[-2:-12:-2]
s3=slice(5)
s4=slice(-1,-16,-3)
print(s1)
print(s2.lower())
print(string[s3].upper())
print(string[s4].lower())

lis=[]
for i in range(0,len(string)):
    lis.append(string[i])
print(lis)
lis.pop()
print(lis)
lis.insert(1,"start")
print(lis)