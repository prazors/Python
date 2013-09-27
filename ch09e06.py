junk = [3, 7, 9, 10, 13, 17, 21, 24, 27]
a=2
b=-1

"""
  >>> 13 in junk
  True
  >>> del junk[4]
  >>> junk
  [3, 7, 9, 10, 17, 21, 24, 27]
  >>> del junk[a:b]
  >>> junk
  [3, 7, 27]
"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()
