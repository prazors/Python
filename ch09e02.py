def my_list():
"""
  >>> a_list[3]
  42
  >>> a_list[6]
  'Ni!'
  >>> len(a_list)
  8
"""
#a_list=['boss','incompetent','Santi',42,'hate','poverty','Ni!', 'FUUCKKKK!']
"""
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""
b_list=["Quarles",'Stills','Nash']
c_list=["Atwood", "Gerfaud","Obrien", "Young"]
"""
        >>> 'war' in mystery_list
        False
        >>> 'peace' in mystery_list
        True
        >>> 'justice' in mystery_list
        True
        >>> 'oppression' in mystery_list
        False
        >>> 'equality' in mystery_list
        True
"""  
if __name__ == '__main__':
    import doctest
    doctest.testmod()
