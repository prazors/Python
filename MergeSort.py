#!/usr/bin/python

import time
import sys
import random

# Subroutine: merge
# Input: two arrays, the left and right halves of
#        the array to be sorted
# Output: a single array that merges left and right,
#         in sorted order
#
def merge( left, right ):
    # Initialize return array, will contain the merged left & right sides
    result = []

    # Initialize loop variables i and j
    # (Python pro-tip: unlike java, we don't need
    # to declare i and j as integers)
    i, j = 0, 0

    # Move i and j through their respective arrays
    # Compare each element from left and right
    # Whichever is lower gets appended to result first
    # Once you've appended something from left, increment i
    # Once you've appended something from right, increment j

    # Python pro-tip: Parens around conditional statements
    # are not required. Coding convention is to skip them.
    while i < len( left ) and j < len( right ) :
        if left[i] <= right[j] :
            result.append( left[i] )
            i += 1
        else:
            result.append( right[j] )
            j += 1
    
    # Make sure result also contains anything leftover
    # not already captured from left, right
    #
    # python pro-tip:
    # left[i:] is everything after i in "left"
    result += left[i:]
    result += right[j:]

    return result
        
# Subroutine: mergesort
# Input: array to be sorted
# Output: sorted list
# 
# This is a recursive subroutine.
# Base case: length of input array <= 1. Return array.
# Gen'l case: split array into left and right halves, call merge subroutine

def insertion_sort( lst):
    for i in range(1, len( lst)):       #for each element in the list ranging from 1 to length of list
        save = list[ i ]                # store each element in save
        j = 1

        while j > 0 and lst[j - 1] > save:          #while j is greater than zero AND the element in list is bigger than save
            lst[ j ] = lst[ j - 1 ]                 #swap elements
            j -= 1                                  #decrement j
        lst[ j ] = save
        return lst

def mergesort( lst ):

    # Base case: length of input <= 1
    if len( lst ) <= 1:
        return lst
            
    THRESHOLD = 9

    # Find the middle of the input array
    # Split in half, into left and right arrays
    # 
    # Python pro-tip: lst[ :middle ] returns
    # everything in the array, from 0 to middle
    if len( lst ) <= THRESHOLD:
        insertion_sort( lst )

    middle = int( len( lst ) / 2 )
    left = mergesort(lst[ :middle ])
    right = mergesort(lst[ middle: ])

    # Return the call to merge on left and right
    return merge(left, right)
        

##this is the test section
if __name__ == "__main__":

    k = 0
    myArr = []
    myArr2 = []
    myArr3 = []

    while k < 100:
        myArr.append( random.randrange(0, 100) )
        k += 1

    k = 0

    while k < 1000:
        myArr2.append( random.randrange(0, 100) )
        k += 1

    k = 0

    while k < 10000:
        myArr3.append( random.randrange(0, 100) )
        k += 1



    
    sorted = mergesort(myArr)
    print (sorted)

    sorted = mergesort(myArr2)
    print (sorted)

    sorted = mergesort(myArr3)
    print (sorted)
