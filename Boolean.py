a = 3
b = 6
s = "SuvarnaShiva"

# Using in a normal print statement
print(3 > 9)

# Below statements print True
print(bool(True))
print(bool("SuvarnaShiva"))
print(bool('P'))
print(bool({3,6,9}))
print(bool(["SS", 3, 'M']))

# Below statements print False
print(bool(False))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
print(bool(""))
print(bool(''))

# Using with variables
print(a < b)

# Using in If statement
if "a" in "apple":
    print("Yes, it is present")
else:
    print("False")

# Some boolean methods
print(isinstance(a, int))
print(isinstance(s, str))
print(isinstance(b, bool))
print(a.__or__(b), b.__and__(a))
print("This prints the given value+1 with negative symbol:", a.__invert__(), b.__invert__())
