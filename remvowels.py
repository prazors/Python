def remvowels(s):
    vowels="aeiouAEIOU"
    cons=""
    for letter in s:
        if letter not in vowels:
            cons += letter
    return cons
        
