# Syntax of a List
fav_numbers = [3, 6, 9, 12, 15, 18]
u = "\nLists:"
print(u.upper())
print("My data type is:", type(fav_numbers))
List = ['p', 6, "SuvarnaShiva", 6.0, 3 + 0j, True]
print("List containing multiple data types:", List)

# List Constructor
u1 = "\nList Constructor:"
print(u1.upper())
a = "SuvarnaShiva"
print("Conversion of String to List:", list(a))

# Allows Duplicate values and are mutable
l = [3, 3, 6, 6, 9, 9]
print("I have duplicate values:", l)
l = [3, 6, 9]
print("I am modified:", l)

# Accessing data:
u2 = "\nAccessing data in list:"
print(u1.upper())
# By using index
colors = ["Pink", "Blue", "Violet", "Purple", "Orange", "White", "Black"]
print("Accessing third element:", colors[2])
# By using negative index
print("Accessing last third item using negative indexing:", colors[-3])
# By using range
print("Using range:", colors[2:6])
print("Leaving starting range:", colors[:3])
print("Leaving ending range:", colors[3:])
# By using negative range
print("Using negative indexing in range:", colors[-3:-1])
print("Leaving starting range:", colors[:-4])
print("Leaving ending range:", colors[-3:])
# By using if statement
if "Blue" in colors:
    print("Yes, I'm Blue.")
else:
    print("No, i am not.")

# Adding to a list
u3 = "\nAdding in a list:"
print(u3.upper())
Clothing = ["Jumpsuits", "Co-Ords", "Dresses", "Frocks", "Jeans", "Skirts", "Shirts"]
# Using Index
Clothing[3] = "NightSuit"
print("Using_Index:")
print("All Western Wear:", Clothing)
# Using Slicing Method
Clothing[0:2] = "Anarkali", "Chudidhaar"

print("Using Slicing_Method:")
print("Sanatani Clothing included:", Clothing)
# Using negative slicing
Clothing[-5:] = "Saree", "Punjabi Dress", "Sharara", "Half Saree", "Lehenga"
print("Using Negative_Slicing:")
print("Clothing changed to Bharat wear:", Clothing)
# Using Insert Method
Clothing.insert(3, "Pattu Langa")
print("Using Insert_Method:")
print("Clothing:", Clothing)
# Using Append Method
Clothing.append("Langa Voni")
print("Using Append_Method:")
print(Clothing)
# Using Extend Method
Clothes = ("Ghaghra Choli", "Kurta Set", "Kurti")
Clothing.extend(Clothes)
print("Using Extend_Method:")
print("We have extended Clothing:", Clothing)
Lis = [3, 6, 9]

# Using Reverse Method:
u4 = "\nReverse Method:"
print(u4.upper())
Lis.reverse()
print("Using Reverse_Method:", Lis)
# Using Reversed Method:
Li = [3, 6, 9]
Li_N = reversed(Li)
print("Using Reversed_Method:", Li_N)
print(set(Li_N))
print(tuple(Li_N))                            # in an iterator format
print(list(Li_N))                             # can be converted to list,tuple,dictionary,set

# Removing in a list
u5 = "\nRemoving in a list:"
print(u5.upper())
n = [3, 6, 9, 12, 15, 18, 21]
print("The Numbers:", n)
n.remove(18)
print("Removing number 18:", n)
# Removing in a loop
'''
n = [3, 6, 9, 12, 15, 18, 21]
print(n)
for i in range(3, len(n)):
    n.remove(i)
print("Loop", n)
'''
# Removing using Pop Method
n.pop(3)
print("Removing number 12 using pop method:", n)
# Using Pop Method in a List
'''
pm = [3, 6, 9, 12, 15, 18, 21]
p = len(pm)
for i in range(3, 5):
    pm.pop(i)
print("Used Pop Method in a loop:", pm)
'''
# Removing using del method
d = ["Silk", "Cotton", "Rayon", "Satin", "Nylon", "Khadi"]
del d[2]
print("Rayon is deleted using delete method:", d)
# Clearing using clear method
c = ["Dark", "Light", "Bright"]
print("List before using clear method:", c)
c.clear()
print("The list is cleared using clear method:", c)

# Lists in loop
u5 = "\nIn Loops:"
print(u5.upper())
# Looping through an ordinary for loop
chocolates = ["DairyMilk", "5Star", "MilkyBar", "BarOne", "KitKat", "Nestle"]
print("Looping through for loop:")
for i in chocolates:
    print(i)
# Looping through a range of index numbers
sweets = ["Rasgulla", "KalaJamun", "GulabJamun", "Rasmalai"]
print("The indexes of the list are:")
for i in range(len(sweets)):
    print(i)
# Looping through while loop
vegetables = ["Potato", "Carrot", "Beetroot", "Lettuce", "Tomato"]
print("Looping through While Loop:")
i = 0
while i < len(vegetables):
    print(vegetables[i])
    i = i+1
# Looping through List Comprehension
floors = ["Third Floor", "Sixth Floor", "Ninth Floor", "Twelfth Floor"]
print("Looping through List Comprehension:")
[print(x) for x in floors]

# List Comprehension
# Creating a new list from the old list
u6 = "\nIn List Comprehension:"
print(u6.upper())
metals = ["Iron", "Steel", "Copper", "Brass", "Gold"]
new_metal = [x if x != "Copper" else "Aluminium(replaced metal)" for x in metals]
print(new_metal)
# Using range to print numbers from 1 to 10
num = [x for x in range(11)]
print("Numbers from 1 to 10 are:", num)
# Using range to print numbers greater than 3
num = [x for x in range(11) if x > 3]
print("Numbers greater than 3 are:", num)
# Using
bags = ["Hand Bags", "Sling Bags", "Tote Bags"]
ba = bags.append("Shoulder Bags" for x in bags)
print(ba)

# Sorting List
u7 = "\nSorting List:"
print(u7.upper())
digits_ = [3, 60, 90, 21, 15, 30, 9, 6]
digits_.sort()
print("Sorted to Ascending order:", digits_)
digits_.sort(reverse= True)
print("Sorted to Descending order:", digits_)
five = ["Fire", "earth", "Air", "water", "sky"]
five.sort()
print("Sorting lists are case sensitive:", five)
five.sort(key=str.lower)
print("Sorting lists will be Case Insensitive:", five)
five.reverse()
print("List Sorting will print in reverse:", five)

# Copying List
u8 = "\nCopying List:"
print(u8.upper())
candy = ["Mango Bite", "KissMi", "Melody", "Choco Plus", "Eclairs", "Kaccha Mango"]
candy_1 = candy
print("This is candy:", candy, "\nThis is a copy of candy_1", candy_1)
candy.append("Milky Bar")
print("This is candy:", candy, "\nThis is a copy of candy_1", candy_1)
# Using copy method:
candy_3 = candy.copy()
print("This is candy:", candy, "\nThis is a copy of candy_3", candy_3)
candy.remove("Choco Plus")
print("This is candy:", candy, "\nThis is a copy of candy_3", candy_3)
# Using list method:
fingers = ["First Finger", "Second Finger", "Fourth Finger", "Sixth Finger"]
fingers_c = list(fingers)
print("This is fingers:", fingers, "\nThis is a copy of fingers:", fingers_c)
fingers[3] = "Fifth Finger"
print("This is fingers:", fingers, "\nThis is a copy of fingers:", fingers_c)
fingers_c.insert(2, "Third Finger")
print("This is fingers:", fingers, "\nThis is a copy of fingers:", fingers_c)

# Joining Lists
u9 = "\nJoining Lists:"
print(u9.upper())
one = [3, 6, 9, 12]
two = [15, 18, 21, 24]
three = [27, 30, 33, 36]
four = [39, 42, 45, 48]
# Joining through Concatenation
one_two = one + two
print("Concatenating Lists:", one_two)
# Joining through append
two_three = two.append(one_two)
print("Joining through append method:", one_two)
# Joining through extend
three.extend(four)
print("Joining through extend method:", three)


