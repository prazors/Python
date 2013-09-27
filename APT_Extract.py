def extract(oldfile, newfile):
    infile = open(oldfile, 'r')
    outfile = open(newfile, 'w')
    while True:
        text = infile.readline()
        if text == "":
           break
        if text[0:3] != 'APT':
           continue
        if text[14:21] != 'AIRPORT':
            continue
        outfile.write(text)
    infile.close()
    outfile.close()
    return
def getid():
    infile = open
