def move(strng):
    start = 1
    step = start + 1
    head = strng[:start]
    midd = strng[start:step]
    tail = strng[step:]

    return tail + midd + head

    
