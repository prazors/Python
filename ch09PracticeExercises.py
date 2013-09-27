def add_vectors(u,v):# this fucntion is pure
    nl = u
    for i in range(len(u)):
        nl[i] = u[i] + v[i]
    print nl

def scalar_mult(s, v): # this fucntion is pure
    """
      >>> scalar_mult(5, [1, 2])
      [5, 10]
      >>> scalar_mult(3, [1, 0, -1])
      [3, 0, -3]
      >>> scalar_mult(7, [3, 0, 5, 11, 2])
      [21, 0, 35, 77, 14]
    """
    nl = v
    for e in range(len(v)):
        nl[e] = s*(v[e])
    return nl

def dot_product(u, v):
    """
      >>> dot_product([1, 1], [1, 1])
      2
      >>> dot_product([1, 2], [1, 4])
      9
      >>> dot_product([1, 2, 1], [1, 4, 3])
      12
      >>> dot_product([2, 0, -1, 1], [1, 5, 2, 0])
      0
    """
    nl = 0
    for i in range(len(u)):
        nl = nl + (u[i] * v[i])
    print nl
    
