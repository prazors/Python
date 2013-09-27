def range1(a,b,c):
    a=5
    b=18
    c=4
    """
  >>> range(a, b, c)
  [5, 9, 13, 17]
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod()

def this():
    this = ['I', 'am', 'not', 'a', 'crook']
    that = ['I', 'am', 'not', 'a', 'crook']
    print "Test 1: %s" % (this is that)
    that = this
    print "Test 2: %s" % (this is that)
