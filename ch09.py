def num1():
    numbers=[1, 2, 3, 4, 5]
    
    for number in numbers:
        numbers[number] = numbers[number]**2
    print numbers

def num2():
    

    for index, v in enumerate(['banana', 'apple', 'pear', 'quince']):
        numbers[index] = v**2
    print index, v
    
def double_stuff(a_list): #this function changes the parameter
    for index, value in enumerate(a_list):
        a_list[index] = 2 * value

def double_stuff2(a_list): #this function does not change the parameter
    new_list = []
    for value in a_list:
        new_list += [2 * value]
    return new_list

def makematrix(rows, columns): #this doctest would fail
#    """
#      >>> makematrix(3, 5)
#      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#      >>> makematrix(4, 2)
#      [[0, 0], [0, 0], [0, 0], [0, 0]]
#      >>> m = makematrix(4, 2)
#      >>> m[1][1] = 7
#      >>> m
#      [[0, 0], [0, 7], [0, 0], [0, 0]]
#    """
    return [[0] * columns] * rows


def makematrix2(rows, columns): #this doctest would not fail
    """
      >>> makematrix2(3, 5)
      [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
      >>> makematrix(4, 2)
      [[0, 0], [0, 0], [0, 0], [0, 0]]
      >>> m = makematrix2(4, 2)
      >>> m[1][1] = 7
      >>> m
      [[0, 0], [0, 7], [0, 0], [0, 0]]
    """
    matrix=[]
    for row in range(rows):
        matrix = matrix + [[0] * columns]
    return matrix

def trav (mylist):
    mylist=list(mylist)
    count=0
    for elem in mylist:
        for ch in elem:
            count+=1
        print count
        count=0

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
