def jack(prefixes):
    suffix = "ack"
    mid = 'u'
    for letter in prefixes:
        if letter not in 'OQ':
            print letter + suffix
        else:
             print letter + mid + suffix
    
            
