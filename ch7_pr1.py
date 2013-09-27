o = 'Ou'
q = 'Qu'

prefixes = "JKLMN%sP%s" % (o,q)
suffix = "ack"

for letter in prefixes:
    print letter + suffix
