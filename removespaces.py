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

def trimsert(text,char):
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
    #inserts a ch between each visible character in a string
 
    newl = []
    flist = []
    sube = []
    for e in str.split(mystring):
        #splits my text into ['this', 'is', 'killing', 'me']
        #loops each element in ['this', 'is', 'killing', 'me']

        subl = list(e)
        # make a sublist out of each element

        for i in subl:
            #for each i inside of subl (sublist)

            if i <> subl[len(subl)-1]:
            # if i in sublist is not the last element, then
            # insert a hyphen
                sube += [i+ch]

            else:
                sube += [i]
            # else if i is the last element then simply add i to the 
            # sublist 

        newl += [''.join(sube)]
        #join the sub element list into a string and add it as
        # as an element to the newlist

        sube = []
        #sets sub element back to empty list

    flist += newl
    #appends the newl list to the flist

    return '  '.join(flist)
                    
        

            





        
