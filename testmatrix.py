def testmatrix(m1,m2):
##    """
##      >>> a = [[1,2]]
##      >>> b = [[2,2]]
##      >>> testmatrix(a, b)
##      >>> [[3, 4]]
##   """
##    i = 0
##    newmatrix = []    
##    for e in m1[i]:
##        newmatrix[i] = newmatrix[i] + [e + m2[i]]
##        i += 1
##    return newmatrix
##    newmatrix = []
##    i = 0
##    e2 = 0
##    for e in m1:
##        newmatrix = [newmatrix + [m1[i][e2] + m2[i][e2]]]
##        i += 1
##        e2 += 1
##    return newmatrix
##    i = 0
##    e = 0
##    
##    newmatrix = []
##    for el in m1[i]:
##        newmatrix = newmatrix + [m1[i][e] + m2[i][e]]
##        i += 1
####        e += 1
##    return newmatrix
    
            

if __name__ == '__main__':
    import doctest
    doctest.testmod()
