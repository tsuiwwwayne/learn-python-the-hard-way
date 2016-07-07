# Learn Python the Hard Way
# Exercise 17 - File Copy

from sys import argv
from os.path import exists

script, from_file, to_file = argv

##### Textbook version #####
# print "Copying from %s to %s." % (from_file, to_file)
#
# in_file = open(from_file)
# indata = in_file.read()
#
# print "The input file is %d bytes long" % len(indata)
#
# print "Does the output file exist? %r" % exists(to_file)
# print "Ready, hit return to continue, CTRL-C to abort."
# raw_input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print "Alright, all done."
#
# out_file.close()
# in_file.close()


##### Shorter version #####
inData = open(from_file).read()

if exists(to_file):
    open(to_file, 'w').write(inData)
    print "Successfully copied from '%s' to '%s'." % (
        from_file, to_file
    )
else:
    print "Designated file '%s' does not exist." % to_file
