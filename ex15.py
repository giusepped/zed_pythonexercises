# adds argument variables to this program
from sys import argv

# 'unpacks' the arguments, assigning them to script and filename
script, filename = argv

# this is a function that opens 'filename and assigns it to txt
txt = open(filename)

print "Here's your file %r:" % filename
# this is a function that takes txt and reads it
print txt.read()

print "I'll also ask you to type it again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
