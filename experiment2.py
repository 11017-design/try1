a=14
b=4
print(f"""Arithmetic Operator-->
Addition:
{a+b}
{a+complex(4.8+1j)}
{str(a)+str(bool(4.8))}
Subtraction:
{a-b}
{a-bool(2)}
Multiplication:
{a*b}
{"Hello!"*3}
Divistion: {a/b}
Square: {a**2}
Modulus: {a%b}
Floor division: {a//b}
""")

print(f"""\nComparison Operator-->
Less than: {a<b}
Greater than: {a>b}
Less than equal to: {a<=b}
Greater than equal to: {a>=b}
\'==\': {a==b}
not equal to: {a!=b}""")

print(f"""Logical Operator--->
AND: {a and b}
OR: {a or b}
NOT: {not a}
""")

print(f"""Bitwise Operator--->
and (&): {a & b}
or (|): {a | b}
ex- or (^): {a ^ b}
complement (~): {~a}
shift right (>>): {a>>1}
shift left (<<): {a<<1}
""")

print(f"""Identity Operator--->
IS: {a is b}
IS NOT: {a is not b}
""")

x=[10,50,40,90]
print(f"""Membership Operator--->
IN: {a in x}
NOT IN: {a not in x}
{print(ord('a'))}
{print(ord("b"))}
""")
c=2
a="shikha"
print(a)
b="simran"
print(a<b)
print(a>b)
print(a<=b)