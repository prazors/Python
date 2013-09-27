def find(strng, start=0, step=-1):
    start = len(strng)-1
    backwards = ""
    while 0 <= start <= len(strng):
        backwards += strng[start]
        start += step
    return backwards
