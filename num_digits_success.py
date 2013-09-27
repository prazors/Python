def num_digits(n):
    count = 0
    if n>0:
        while n:
            count = count + 1
            n = n / 10
        print count
    else:
        count = 1
        print count
