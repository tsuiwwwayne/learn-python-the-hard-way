# Learn Python the Hard Way
# Exercise 32 - For Loops

the_count = [1, 2, 3, 4 ,5]
fruits = ["apples", "oranges", "pears", "apricots" ]
change = [1, "pennies", 2, "dimes", 3, "quarters" ]

# For loop that goes through a list
for number in the_count:
    print "This is count %d" % number

# Same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can go through lists with multiple types
# Notice we have to use %r since we do not know what is in it

for i in change:
    print "I got %r" % i

# We can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a list function
    elements.append(i)

# Now we can print them out too
for i in elements:
    print "Element was %d" % i
