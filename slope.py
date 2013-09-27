from __future__ import division
def slope(y2, y1, x2, x1):
    """
      >>> slope(5, 3, 4, 2)
      1.0
      >>> slope(1, 2, 3, 2)
      0.0
      >>> slope(1, 2, 3, 3)
      0.5
      >>> slope(2, 4, 1, 2)
      2.0
    """
    n=(y2-y1)
    d=(x2-x1)

    print n / d
if __name__ == '__main__':
    import doctest
    doctest.testmod()

