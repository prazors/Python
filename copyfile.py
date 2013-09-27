def copy_file(oldfile, newfile):
    sourcefile = open(oldfile, 'r')
    destfile = open(newfile, 'w')
    while True:
        text = sourcefile.read(50)
        if text == "":
            break
        destfile.write(text)
    sourcefile.close()
    destfile.close()
    return
