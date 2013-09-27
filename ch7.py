fruit = 'ramalama'
def r():
    """
        >>> type(fruit)
        <type 'str'>
        >>> len(fruit)
        8
        >>> fruit[:3]
        'ram'
    """
    
    return fruit

if __name__ == '__main__':
        import doctest
        doctest.testmod()
        
