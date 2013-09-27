def filter(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.readline()
        if text == "":
           break
        if text[0] == '#':
           continue
        outfile.write(text)
    infile.close()
    outfile.close()
    return
