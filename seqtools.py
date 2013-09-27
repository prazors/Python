def remove_at(pos, seq):
    return seq[:pos] + seq[pos+1:]

def insert_in_middle(val, lst):
    # inserts a value 'val' in middle of list 'lst'..works on lists only
    middle = len(lst)/2
    lst[middle:middle] = [val]

def insert_in_middle(val, tup):
    # same as above, but works for tuples only
    middle = len(tup)/2
    return tup[:middle] + (val,) + tup[middle:]

def recursive_max(nested_num_list):
    """
      >>> recursive_max([2, 9, [1, 13], 8, 6])
      13
      >>> recursive_max([2, [[100, 7], 90], [1, 13], 8, 6])
      100
      >>> recursive_max([2, [[13, 7], 90], [1, 100], 8, 6])
      100
      >>> recursive_max([[[13, 7], 90], 2, [1, 100], 8, 6])
      100
    """
    largest = nested_num_list[0]
    while type(largest) == type([]):
        largest = largest[0]

    for element in nested_num_list:
        if type(element) == type([]):
            max_of_elem = recursive_max(element)
            if largest < max_of_elem:
                largest = max_of_elem
        else:                           # element is not a list
            if largest < element:
                largest = element

    return largest

def recursive_min(nested_num_list):
##    """
##      >>> recursive_min([2, 9, [1, 13], 8, 6])
##      1
##      >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
##      1
##      >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
##      -7
##      >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
##      -13
##    """
    smallest = nested_num_list[0]
    while type(smallest) == type([]):
        smallest = smallest[0]

    for e in nested_num_list:
        if type(e) == type([]):
            min_of_e = recursive_min(e)
            if smallest < min_of_e:
                min_of_e = smallest
    else:
        if smallest > e:
            smallest = e
    return smallest


def encapsulate(val, seq): #helper function that encapsulates
                            # to return the correct seq type
    """
      >>> encapsulate('2','01')
      '2'
      >>> encapsulate('2',[0,1])
      ['2']
      >>> encapsulate(2,(1,2))
      (2,)
    """
    if type(seq) == type(""):
        return str(val)
    if type(seq) == type([]):
        return [val]
    return (val,)

def insert_in_middle(val, seq):#uses aformetioned encapsulate to get
                            #proper value
    """
      >>> insert_in_middle(2, [0, 1, 3, 4])
      [0, 1, 2, 3, 4]
      >>> insert_in_middle(2, '0134')
      '01234'
      >>> insert_in_middle(2, (0,1,3,4))
      (0, 1, 2, 3, 4)
    """
    middle = len(seq)/2
    return seq[:middle] + encapsulate(val, seq) + seq[middle:]

def make_empty(seq):
    """
      >>> make_empty([1, 2, 3, 4])
      []
      >>> make_empty(('a', 'b', 'c'))
      ()
      >>> make_empty("No, not me!")
      ''
    """
    if type(seq) == type(""):
        return ''
    if type(seq) == type([]):
        return []
    return ()

def insert_at_end(val, seq):
    """
      >>> insert_at_end(5, [1, 3, 4, 6])
      [1, 3, 4, 6, 5]
      >>> insert_at_end('x', 'abc')
      'abcx'
      >>> insert_at_end(5, (1, 3, 4, 6))
      (1, 3, 4, 6, 5)
    """
    seq = seq[:] + encapsulate(val, seq)
    return seq

def insert_in_front(val, seq):
    """
      >>> insert_in_front(5, [1, 3, 4, 6])
      [5, 1, 3, 4, 6]
      >>> insert_in_front(5, (1, 3, 4, 6))
      (5, 1, 3, 4, 6)
      >>> insert_in_front('x', 'abc')
      'xabc'
    """
    seq = encapsulate(val, seq) + seq[:]
    return seq

def index_of(val, seq, start=0):
    """
      >>> index_of(9, [1, 7, 11, 9, 10])
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5))
      3
      >>> index_of(5, (1, 2, 4, 5, 6, 10, 5, 5), 4)
      6
      >>> index_of('y', 'happy birthday')
      4
      >>> index_of('banana', ['apple', 'banana', 'cherry', 'date'])
      1
      >>> index_of(5, [2, 3, 4])
      -1
      >>> index_of('b', ['apple', 'banana', 'cherry', 'date'])
      -1
    """
    count = 0
    seq = seq[start:]
    for e in seq:
        
        if e == val:
            return count + start
        count += 1
    return -1

def remove_part(index, seq):
    """
      >>> remove_part(3, [1, 7, 11, 9, 10])
      [1, 7, 11, 10]
      >>> remove_part(5, (1, 4, 6, 7, 0, 9, 3, 5))
      (1, 4, 6, 7, 0, 3, 5)
      >>> remove_part(2, "Yomrktown")
      'Yorktown'
    """
    seq = seq[:index] + seq[index+1:]
    return seq

def remove_val(val, seq):
    """
      >>> remove_val(11, [1, 7, 11, 9, 10])
      [1, 7, 9, 10]
      >>> remove_val(15, (1, 15, 11, 4, 9))
      (1, 11, 4, 9)
      >>> remove_val('what', ('who', 'what', 'when', 'where', 'why', 'how'))
      ('who', 'when', 'where', 'why', 'how')
    """
    index = -1
    for e in seq:
        index += 1
        if e == val:
            break
    return seq[:index] + seq[index+1:]
            
def remove_all(val, seq):
    """
      >>> remove_all(11, [1, 7, 11, 9, 11, 10, 2, 11])
      [1, 7, 9, 10, 2]
      >>> remove_all('i', 'Mississippi')
      'Msssspp'
    """
    if type(seq) == type(''):
        return ''.join([e for e in seq if e != val])
    if type(seq) == type(()):
        return tuple([e for e in seq if e != val])
    return [e for e in seq if e != val]

def count(val, seq):
    """
      >>> count(5, (1, 5, 3, 7, 5, 8, 5))
      3
      >>> count('s', 'Mississippi')
      4
      >>> count((1, 2), [1, 5, (1, 2), 7, (1, 2), 8, 5])
      2
    """
    count = 0
    for e in seq:
        if e == val:
            count += 1
    return count
##def reverse(seq):
##    """
##      >>> reverse([1, 2, 3, 4, 5])
##      [5, 4, 3, 2, 1]
##      >>> reverse(('shoe', 'my', 'buckle', 2, 1))
##      (1, 2, 'buckle', 'my', 'shoe')
##      >>> reverse('Python')
##      'nohtyP'
##    """

def sort_sequence(seq):
##    """
##      >>> sort_sequence([3, 4, 6, 7, 8, 2])
##      [2, 3, 4, 6, 7, 8]
##      >>> sort_sequence((3, 4, 6, 7, 8, 2))
##      (2, 3, 4, 6, 7, 8)
##      >>> sort_sequence("nothappy")
##      'ahnoppty'
##    """
#partial credit on this frustrating bullshit
    step = 0
    nl = []
    

    for e in seq:
        if e >= seq[step]:
            seq = seq[step+1:] + seq[:step+1]
            step += 1

    return seq[1:] + seq[:1]


def sortseq(seq):
##    """
##      >>> sortseq([3, 4, 6, 7, 8, 2])
##      [2, 3, 4, 6, 7, 8]
##      >>> sortseq((3, 4, 6, 7, 8, 2))
##      (2, 3, 4, 6, 7, 8)
##      >>> sortseq("nothappy")
##      'ahnoppty'
##    """

 
    
    for e in seq:
        if e <> min(seq):
             
            seq += [e]
            seq = seq[1:]
            
            sortseq(seq)
        else:
            seq  = [seq] + [e]
                
            
            
    return seq
            
            
    

        




















            
            


        
   

            
if __name__ == '__main__':
    import doctest
    doctest.testmod()

