def add_row(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_row(m)
      [[0, 0], [0, 0], [0, 0]]
      >>> n = [[3, 2, 5], [1, 4, 7]]
      >>> add_row(n)
      [[3, 2, 5], [1, 4, 7], [0, 0, 0]]
      >>> n
      [[3, 2, 5], [1, 4, 7]]
    """
    newmatrix = []
    for e in range(len(matrix[0])):
        newmatrix = newmatrix+[e*0]
    return matrix + [newmatrix]

def add_column(matrix):
    """
      >>> m = [[0, 0], [0, 0]]
      >>> add_column(m)
      [[0, 0, 0], [0, 0, 0]]
      >>> n = [[3, 2], [5, 1], [4, 7]]
      >>> add_column(n)
      [[3, 2, 0], [5, 1, 0], [4, 7, 0]]
      >>> n
      [[3, 2], [5, 1], [4, 7]]
    """
    i = 0
    newmatrix = []
    for e in matrix:
        #newmatrix = newmatrix + [matrix[i] + [0]]
        #i += 1
        newmatrix = newmatrix + [e + [0]]
    return newmatrix

def add_matrices(m1, m2):

    e = 0
    i = 0
    nr = []
    nm = []
    step = 0
    while e < len(m1):
        if e < len(m1):
            nr = nr + [m1[step][i] + m2[step][i]]
            i += 1
            e += 1
        e = 0
        step += 1

        
    print nr


    




            
##    """
##      >>> a = [[1, 2], [3, 4]]
##      >>> b = [[2, 2], [2, 2]]
##      >>> add_matrices(a, b)
##      [[3, 4], [5, 6]]
##      >>> c = [[8, 2], [3, 4], [5, 7]]
##      >>> d = [[3, 2], [9, 2], [10, 12]]
##      >>> add_matrices(c, d)
##      [[11, 4], [12, 6], [15, 19]]
##      >>> c
##      [[8, 2], [3, 4], [5, 7]]
##      >>> d
##      [[3, 2], [9, 2], [10, 12]]
##   """





##    nm = []
##    nl = []
##    index = 0
##    i = 0
##    while index < len(m1):
##        for e1, e2 in m1[index], m2[index]:
##            nl = [e1] + [e2]
####            print [e1, e2]
####            print e1[i] + e2[i]
##        index += 1
##    return nl
####        i += 1
####        nm = nm +[nl]
####        nl = []
####    return nm
        



def scalar_mult(s, m):
    """
      >>> a = [[1, 2], [3, 4]]
      >>> scalar_mult(3, a)
      [[3, 6], [9, 12]]
      >>> b = [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
      >>> scalar_mult(10, b)
      [[30, 50, 70], [10, 10, 10], [0, 20, 0], [20, 20, 30]]
      >>> b
      [[3, 5, 7], [1, 1, 1], [0, 2, 0], [2, 2, 3]]
    """
    nm = []
    nl = []
    e = 0
    for i in m:
        while e < len(i):
            nl = nl + [s*(i[e])]
            e += 1
        nm += [nl]
        nl = []
        e = 0
    return nm

##def row_times_column(m1, row, m2, column):
##    """
##      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 0)
##      19
##      >>> row_times_column([[1, 2], [3, 4]], 0, [[5, 6], [7, 8]], 1)
##      22
##      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 0)
##      43
##      >>> row_times_column([[1, 2], [3, 4]], 1, [[5, 6], [7, 8]], 1)
##      50
##    """

def newcolumn(m2, column):
    """
        >>> newcolumn([[5,6], [7, 8]], 0)
        [5, 7]
    """
    
    nc = []
    for i in m2:
        e = i[column]
        nc += [e]
    return nc
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
