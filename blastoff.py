def blastoff(n):
    if n == 0:
        print 'blastoff!'
    else:
        print n
        blastoff(n-1)
