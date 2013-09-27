def my_list():

"""
  >>> b_list[1:]
  ['Stills', 'Nash']
  >>> group = b_list + c_list
  >>> group[-1]
  'Young'
"""
b_list=["Quarles",'Stills','Nash']
c_list=["Atwood", "Gerfaud","Obrien", "Young"]
 
if __name__ == '__main__':
    import doctest
    doctest.testmod()
