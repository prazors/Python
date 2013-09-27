def reverse(strng,start=0, step=-1):
    """
      >>> reverse('happy')
      'yppah'
      >>> reverse('Python')
      'nohtyP'
      >>> reverse("")
      ''
      >>> reverse("P")
      'P'
    """
    start = len(strng)-1
    strng2=""
    while 0 <= start <= len(strng):
        strng2 += strng[start]
        start += step
    return strng2
if __name__ == '__main__':
    import doctest
    doctest.testmod()
            
    
        
    
        
        
