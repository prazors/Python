def remspaces(text):
                    #takes a string
                    #each character into a string
                    #removes its white space and returns it as a string
    nl = []         
    for ch in text:
        if ch <> ' ':
            nl += ch
        else:
            continue
        
    return ''.join(nl)

def linsert(mylist,ch):

                    #takes a list and adds a ch in between each
                    #element and returns it as a string
    i = 0
    nl = []

    for e in mylist:
        if e <> mylist[len(mylist)-1]:
            nl += [e+ch]
            
        else:
            nl += [e]
                              
    return ''.join(nl)

def trimsert(text,char='-'):
                    #takes a string
                    #removes its white space
                    #inserts ch each character into a string
                    #returns it as a string
                    
    newlist = []
    for ch in text:
        if ch == ' ':
            continue
        newlist += ch
    i = 0
    nl = []
    for e in newlist:
        if i < len(newlist)-1:
            i += 1
            nl += [e+char]
        else:
            nl += [e]
    return ''.join(nl)
        
def insert(mystring, ch):
    #inserts a ch in-between 2 or more visible characters in a string
    step = 0
    newl = []
    flist = []
    sube = []
    for e in str.split(mystring):
        #splits mystring into ['this', 'is', 'killing', 'me']
        #loops each element in ['this', 'is', 'killing', 'me']

        subl = list(e)
        # make a sublist (subl) from each element

        for i in subl:
            #within each element of subl evaluate statement below
            if step < len(subl)-1:
                sube += [i + ch]
                step += 1
                #if step is less than the length of subl
                #then sube is equal to sube + (i + ch)
                #increment the step
            else:
                sube += [i]
                subl = []
                step = 0
                #if not (i.e. at the end of the subl),
                #then append the last element,
                #set subl to an empty list,
                #and reset step back to 0
                #go back to the original for loop
                            
        newl += [''.join(sube)]
        #join the sub element list into a string and add it as
        # as an element to the newlist

        sube = []
        #sets sub element back to empty list

    flist += newl
    #appends the newl list to the flist

    return '  '.join(flist)

##def remove_all(sub, s):
##    """
##      >>> remove_all('an', 'banana')
##      'ba'
##      >>> remove_all('cyc', 'bicycle')
##      'bile'
##      >>> remove_all('iss', 'Mississippi')
##      'Mippi'
##      >>> remove_all('eggs', 'bicycle')
##      'bicycle'
##    """
##    step = 0
##    start = 0
##    emptystr = ''
##
##    for i in s:

def replace(s, old, new):
    """
      >>> replace('Mississippi', 'i', 'I')
      'MIssIssIppI'
      >>> s = 'I love spom!  Spom is my favorite food.  Spom, spom, spom, yum!'
      >>> replace(s, 'o', 'a')
      'I lave spam!  Spam is my favarite faad.  Spam, spam, spam, yum!'
    """
    newstring = ''
    count = 0
    for i in s:
        if i != old or new in i:
            newstring += i
        else:
            newstring += new
    return newstring

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

def mirror(strng, start=0, step=1):
    """
      >>> mirror("good")
      'gooddoog'
      >>> mirror("yes")
      'yessey'
      >>> mirror('Python')
      'PythonnohtyP'
      >>> mirror("")
      ''
      >>> mirror("a")
      'aa'
    """
    strng1=""
    while 0 <= start < len(strng):
        strng1 = strng1 + strng[start]
        start += step
    
    step = -1
    start = len(strng)-1
    strng2=""
    while 0 <= start <= len(strng):
        strng2 += strng[start]
        start += step
    return strng1+strng2

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def remove_letter(letter, strng):
    """
      >>> remove_letter('a', 'apple')
      'pple'
      >>> remove_letter('a', 'banana')
      'bnn'
      >>> remove_letter('z', 'banana')
      'banana'
      >>> remove_letter('i', 'Mississippi')
      'Msssspp'
    """

    nolet = ""
    
    for ch in strng:
        if ch <> letter:
            nolet += ch
    return nolet

if __name__ == '__main__':
    import doctest
    doctest.testmod()

def is_palindrome(strng,fstep=0,bstep=-1):
    """
      >>> is_palindrome('abba')
      True
      >>> is_palindrome('abab')
      False
      >>> is_palindrome('tenet')
      True
      >>> is_palindrome('banana')
      False
      >>> is_palindrome('straw warts')
      True
    """
    for ch in strng:
        if ch in strng[fstep]==strng[bstep]:
            fstep = fstep + 1
            bstep = bstep - 1
        else: return False
    return True

if __name__ == '__main__':
    import doctest
    doctest.testmod()


        
