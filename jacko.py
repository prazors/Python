
prefixes = "JKLMACKUQ"
suffix = "ack"
mid = 'u'

for letter in prefixes:
    if letter not in 'OQ':
        print letter + suffix
    elif letter in 'OQ':
        print letter + mid + suffix

            
