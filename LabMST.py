a=10
b=5
print(f"""
Addition(+)= {a+b}
Subtraction(-)= {a-b}
Multiplication(*)= {a*b}
Divistion(/)= {a/b}
Modulus(%)= {a%b}
Floor division(//)= {a//b}
Exponent(**)= {a**2}
""")

a=6
b=9
print(f"""\n
Less than: {a<b}
Greater than: {a>b}
Less than equal to: {a<=b}
Greater than equal to: {a>=b}
equals to: {a==b}
not equal to: {a!=b}\n""")

a=10
b=1
b+=3
print("b+=3:",b)
b-=1
print("b-=1:",b)
b*=2
print("b*=2:",b)
a/=b
print("a/=b:", a)
c=5
print("c=5:",c)

a=2
b=1
print(f"""\nLogical Operator--->
Logical AND: {a and b}
Logical OR: {a or b}
Logical NOT: {not a}
""")

a=5
b=4
print(f"""\nBitwise Operator--->
Bitwise and (&): {a & b}
Bitwise or (|): {a | b}
Bitwise ex- or (^): {a ^ b}
Bitwise complement (~): {~a}
Bitwise shift right (>>): {a>>1}
Bitwise shift left (<<): {a<<1}
""")