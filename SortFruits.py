def sort(sourcefile, destfile):
    import os,sys
    os.chdir('/home/lee/python')
    sys.path.append('/home/lee/python')
    sourcefile = open(sourcefile, 'r')
    destfile = open(destfile, 'w')
    nl = []
    while True:
        text = sourcefile.readline()
        
        if text =='':
            break
        nl += [text]
    nl.sort()
    for e in nl:
        destfile.write(e)
    sourcefile.close()
    destfile.close()
    return
