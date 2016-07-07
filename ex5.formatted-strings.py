# Learn Python the Hard Way
# Exercise 5 - Formatted Strings

my_name = 'Wayne Tsui'
my_age = 22 # not a lie
my_height = 180.0 # centimetres
my_weight = 80.0 # kilograms
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print "Let's talk about %s." % my_name
print "He's about %d centimetres tall." % my_height
print "He's %d kilograms heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# This line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
