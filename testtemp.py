from __future__ import division
i = raw_input("""is the temp C or F? (for example 'C' for Celsius
or 'F' for Fahrenheit)""")
print i
e = "enter the temp"
if i=='F':
    F = input(e)
    C = (F-32)*(5/9)
    print C, "Celsius"
elif i=='C':
    C = input(e)
    F = (C*(9/5))+32
    print F, "Fahrenheit"
else:
    print "scale not supported"
    


    
