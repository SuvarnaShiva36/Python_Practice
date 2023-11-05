# Evaluating the logic in single line
a = 3
b = 6

# Using Ternary Operator
t = a if a > b else b
print("Using ternary operator:", t)

# My own invention(Don't know if it is present or not but i tried it on my own)
f = a if a > b else b, "Not here"
print("Using my own ternary operator:", f)

# Ternary using Tuples
# Syntax: if the given logic is true then (0,1) 1 is printed else 0
Suvarna = "Female"
Shiva = "Male"
print("Ternary using tuples:", (False, True)[Suvarna == "Male"], (True, False)[Shiva == "Female"])


