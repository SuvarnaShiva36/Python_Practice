import random
a = 3                # Integer
b = 6.0              # Float
c = 3+6j             # Complex
print("People call me Integer:", a, "People call me Float:", b, "People call me Complex:", c, sep='\n')

# Conversion of int to float & complex
print("I'm converted from int to float:", float(a), "I'm converted from int to complex:", complex(a), sep='\n')

# Conversion of float to int & complex
print("I'm converted from float to int:", int(b), "I'm converted from float to complex:", complex(b), sep='\n')

# Conversion of float & int to string
a = str('3')
b = str('6.0')
c = str("3+6j")
print("I'm converted from float to string:", b, type(b), "I'm converted from int to string:",
      a, type(a), "I'm converted from complex to string:", c, type(c), sep='\n')

# Conversion of complex to int & float - This gives an error as complex cannot be casted to any other data type
# print(int(c))

# Built-in module to print a random number from the given range
print("Random Number is:", random.randrange(2,8), sep='\n')

# Methods of int
print("Multiply method of int (int).__mul__(int):", (3).__mul__(6))
print("Add method of int (int).__add(int):", (60).__add__(90))
print("Subtract method of int (int).__sub(int):", (180).__sub__(160))
print("True division returns with decimals:", (9).__truediv__(88))
print("Floor division does return only integer:", (9).__floordiv__(88))
print("Modulus method of int (int).__mod__(int):", (10).__mod__(11))
print("Exponential method of int (int).__pow__(int):", (3).__pow__(3))

# Methods of float
print("", (3.0).__add__(6.0))
