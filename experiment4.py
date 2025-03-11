i=-1
while i<=6:
    print(i, end=' ')
    i+=1
print("\n\n")
j=1
while j>=5:
    print(i)
print("\n\n")  
i=1
while i<6:
    print(i, end=' ')
    if i==3:
        break
    i+=1
print("\n\n")    
i=1
while i<6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6.")
print("\n\n")
for x in range(2,30,3):
    print(x)
print("\n\n")
for x in range(6):
    print(x)
else:
    print("finished.")
print("\n\n")    
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
print("\n")   
adj=["red","big","tasty"]
for x in adj:
    for y in fruits:
        print(x,y)
print("\n")       
s="Sahara"
for x in s:
    print(x, end='\t')
print("\n")
s= input("Enter some String:")
i=0
for x in s:
    print("The character present at ", i,"index is :",x)
    i=i+1
print("\n")    
s="Hello"
for i in range(10):
    print(s)
    
