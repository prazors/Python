from __future__ import division
def temp():         #converts fahrenheit to celsius and vice-versa
    i = raw_input("is the temp C or F?")
    print i
    if i=='F':
        F = input("enter the temp")
        C = (F-32)*(5/9)
        print C, "Celsius"
    elif i=='C':
        C = input("enter the temp")
        F = (C*(9/5))+32
        print F, "Fahrenheit"
    else:
        print "scale not supported"

    
    

    
