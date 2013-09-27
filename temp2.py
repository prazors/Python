from __future__ import division
def temp2():
    raw_input("is the temp C or F?")

    if 'F':
        F = input("enter the temp")
        C = (F-32)*(5/9)
        print C, "Celsius"
    elif 'C':
        C = input("enter the temp")
        F = (C*(9/5))+32
        print F, "Fahrenheit"
    else:
        print "scale not supported"
    


    
