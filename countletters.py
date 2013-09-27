#!/usr/bin/idle-python2.6 
def count_letters(fruit, ch):
    count = 0
    for char in fruit:
        if char == ch:
            count += 1
    print count
