p = 9
s = 6
m = 3
m = s
print("Values of m,p,s:", m, p, s, sep=',')
print("This is is equals to operator:", m)
m = 3
print("The value of m:", m)
print("Values of m,p,s:", m, p, s, sep=',')
p += s
print("This is add and operator:", p)
print("Values of m,p,s:", m, p, s, sep=',')
p -= m
print("This is subtract and operator:", p)
print("Values of m,p,s:", m, p, s, sep=',')
s *= m
print("This is multiply and operator:", s)
print("Value of m & p:", m, p)
p /= m
print("This is divide and operator:", p)
print("Values of m,p,s:", m, p, s, sep=',')
print("Floor value:", s // m)
s //= p
print("This is divide(floor) and operator:", s)
print("Values of m,p,s:", m, p, s, sep=',')
s **= m
print("This is exponent and operator:", s)
print("Values of m,p,s:", m, p, s, sep=',')
s %= m
print("This is modulus and operator:", s)
print("Values of m,p,s:", m, p, s, sep=',')
