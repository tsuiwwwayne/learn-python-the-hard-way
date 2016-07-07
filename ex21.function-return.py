# Learn Python the Hard Way
# Exercise 21 - Function Return

def add(a, b):
    print "Adding %d to %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "Lets do some math with just functions"

age = add (20, 2)
height = subtract(200, 20)
weight = multiply(16, 5)
iq = divide(260, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (
    age, height, weight, iq
)

# Function can accept other functions as parameters
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"
