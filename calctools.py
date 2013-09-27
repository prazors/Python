from __future__ import division
def mean(ls):
    total = 0
    count = 0

    for i in ls:
        if type(i) is int:
            total += i
            count += 1
        else:
            return 'non-numeric exists'
    return total/count
    
def median(ls):
    if len(ls)%2 == 0: #evaluates whether list length is even or odd 
        a = (ls[int(round(len(ls)/2))-1] + ls[int(round(len(ls)/2))])/2
        print a
        return 'even numbered list length'
    
    else:
        b = ls[int(round(len(ls)/2))-1]
        print b
        return 'odd numbered list length'


def mysum(mylist):#sums a list of numbers, ignores string elements
    inc = 0
    for e in mylist:
        if type(e) is int or type(e) is float:
            inc += e
        else:
            continue
    return inc

def myrecursivemax(nested_num_list):#doesn't work entirely
                                    # example 2 test doesnt work
##    """
##      >>> myrecursivemax([2, 9, [1, 13], 8, 6])
##      13
##      >>> myrecursivemax([2, [[100, 7], 90], [1, 13], 8, 6])
##      100
##      >>> myrecursivemax([2, [[13, 7], 90], [1, 100], 8, 6])
##      100
##      >>> myrecursivemax([[[13, 7], 90], 2, [1, 100], 8, 6])
##      100
##    """
    maxn = 0
    for element in nested_num_list:
        if type(element) == type([]):
          maxn = myrecursivemax(element)
        elif element > maxn:
            maxn = element
        else:
            continue
    return maxn

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def fibonacci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)




if __name__ == '__main__':
    import doctest
    doctest.testmod()
