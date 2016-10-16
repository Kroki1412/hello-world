import sys

# the following function will determine what the greeting variable should be if a command line argument is entered
# it will take that, else it will be "world"
def whomtoGreating(arguments):
    if len(sys.argv) > 1:
        greeting = arguments[1]
    else:
        greeting = 'World'
    return greeting

#This will show up in the command line. Hello is predifined and the function will return the variable whom to greet.
print ('%s %s%s' % ('Hello',whomtoGreating(sys.argv),'!'))