#
# infinite_recursion.py
#
##def recursion_depth(number):
##    print "Recursion depth number %d." % number
##    recursion_depth(number + 1)



def recursion_depth(number):
    print "Recursion depth number %d." % number
    try:
        recursion_depth(number + 1)
    except:
        print "Maximum recursion depth exceeded."



