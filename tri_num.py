from __future__ import division
def test(n):
    
    while n != 0:
        print n, '    ',n-1
        if n % n-1 ==0:
            n = 0
        else:
            n = n-1
        
    
