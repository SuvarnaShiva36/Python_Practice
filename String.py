# Creating a String and assigning value to it
s = "SuvarnaShiva"
p = "Padma,Shree"
n = 3
set_ = ['3', '6', '9', '12', '15', '18']
list_ = {"Shiva", '3', "6.0", 'p'}
print("These are Strings:", p, s, set_, list_, sep='\n')
print("Slicing with step:", s[3:9:2])

# Multiline String
print("This is a Multi-Line String:")
pa = '''    I love and trust Shiva, 
    he is my father and my mother is parvati. 
    He is my caretaker, he adjusts with my mood swings. 
    He gives me all his love, care and whatnot'''
print(pa)

# Accessing Elements of a string
print("The fourth letter and last letter is:", p[3], p[-1])

# Looping through String
print("I am in Loop:")
for c in "Banana":
    print(c)

# Length of the String
print("The length of String is-", len(s))

# Finding if the element is present
print("Is the element present?", "Shree" in p)

# Finding if the element is present using if statement
if "Shree" in p:
    print("Yes, it is present")

# Checking if not present
print("Is b not there?", "b" not in p)

# Checking if not present using if statement
if "b" not in p:
    print("'b' is not present")

# Printing range of characters or values
print("I'm getting printed from second position to seventh position-", s[2:8])
print("I'm Getting printed from third position to end-", s[2:])
print("I'm Getting printed from beginning to eight position-", s[:9])
print("Using negative indexing to access last-", s[-9:-1])

# Some of the string methods
print("I'm printed in UpperCase-", p.upper())
print("I'm printed in LowerCase-", p.lower())
m = "  SMahesh  "
print("My whitespaces are removed-", m.strip())
d = "duplicate"
print("My first letter gets capitalized-", d.capitalize())
print("I'm getting split-", p.split())
print("I'm getting replaced-", m.replace("S","Suvarna"))

# Concatenation
p = "PadmaShree"
print("Concatenation of strings- " + p + "," + s)

# Concatenation of strings with numbers using Format Method
print("I'm concatenated with an integer with the help of Format method- " + s + " " + format(n))
t = 3
num = 6
w = 9
se = "I'm going to buy {} sets of kurtis with {} rupees each of {}"
print(se.format(t, num, w))
se = "I'm going to buy {2} sets of kurtis with {0} rupees each of {1}"
print(se.format(num, w , t))

# Escape Character\
print("Using escape character \-", "Suvarna\"Shiva\"")
