a=(7,8,9,6,5)
b=list(a)
b[0],b[1]=b[1],b[0]
b.append(4)
b[2]="Hello"
a=tuple(b)
print(a)

t1=(1,3,5,9,10)
t2=(2,4,5,9,12)

z=[i for i in t1 if i in t2]
print(z)

sum_t=tuple(map(lambda x,y:x+y, t1,t2))
print("Sum of two tuples :",sum_t)


diff_t=tuple(map(lambda x,y:y-x, t1,t2))
print("Difference of two tuples :",diff_t)