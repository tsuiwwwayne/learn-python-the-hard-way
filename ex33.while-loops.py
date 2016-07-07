# Learn Python the Hard Way
# Exercise 33 - While Loops

##### Textbook Version #####

# i = 0
# numbers = []
#
# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)
#
#     i += 1
#     print "Numbers now:", numbers
#     print "At the bottom i is %d" % i
#
#
# print "The numbers:"
# for num in numbers:
#     print num,

##### Funtion Application #####

def populate_list(inputList, limit, increValue):
    for i in range(0, limit, increValue):
        inputList.append(i)

def print_list(inputList):
    for i in inputList:
        print i

inputList = []
populate_list(inputList, 100, 5)
print_list(inputList)
