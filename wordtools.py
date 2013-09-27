def cleanword(word):
    """
      >>> cleanword('what?')
      'what'
      >>> cleanword('"now!"')
      'now'
      >>> cleanword('?+="word!,@$()"')
      'word'
    """
    import string
    nolet = ''
    for i in word:
        if i in string.letters:
            nolet += i
    return nolet

def has_dashdash(s):
    """
      >>> has_dashdash('distance--but')
      True
      >>> has_dashdash('several')
      False
      >>> has_dashdash('critters')
      False
      >>> has_dashdash('spoke--fancy')
      True
      >>> has_dashdash('yo-yo')
      False
    """
    dash = '--'

    if dash in s:
        return True
    return False

def extract_words(s):
##    """
##      >>> extract_words('Now is the time!  "Now", is the time? Yes, now.')
##      ['now', 'is', 'the', 'time', 'now', 'is', 'the', 'time', 'yes', 'now']
##      >>> extract_words('she tried to curtsey as she spoke--fancy')
##      ['she', 'tried', 'to', 'curtsey', 'as', 'she', 'spoke', 'fancy']
##    """
    import string
    nw = ''
    nl=[]
    s = list(s)
    for e in s:
        if e in string.letters:
            nw += e
        else:
            nl += [nw]
            nw = ''
    return nl



def wordcount(word, wordlist):
    """
      >>> wordcount('now', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['now', 2]
      >>> wordcount('is', ['now', 'is', 'time', 'is', 'now', 'is', 'the', 'is'])
      ['is', 4]
      >>> wordcount('time', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['time', 1]
      >>> wordcount('frog', ['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['frog', 0]
    """
    count = 0

    for e in wordlist:
        if word != e:
            continue
        else:
            count += 1
    return [word, count]

def wordset(wordlist):
    #evaluates a list of words and returns a list of unique words only
    """
      >>> wordset(['now', 'is', 'time', 'is', 'now', 'is', 'is'])
      ['is', 'now', 'time']
      >>> wordset(['I', 'a', 'a', 'is', 'a', 'is', 'I', 'am'])
      ['I', 'a', 'am', 'is']
      >>> wordset(['or', 'a', 'am', 'is', 'are', 'be', 'but', 'am'])
      ['a', 'am', 'are', 'be', 'but', 'is', 'or']
    """
    nl = []
    for e in wordlist:
        if e in nl:
            continue
        else:
            nl += [e]
    nl.sort()
    return nl

def longestword(wordset):
    #returns the length of the longest word in a wordlist
    """
      >>> longestword(['a', 'apple', 'pear', 'grape'])
      5
      >>> longestword(['a', 'am', 'I', 'be'])
      2
      >>> longestword(['this', 'that', 'supercalifragilisticexpialidocious'])
      34
    """
    counted = 0
    count = 0
    largestcount = 0
    for e in wordset:
        for i in e:
            count += 1
            counted += count
            count = 0
        if counted > largestcount:
            largestcount = counted
            counted = 0
        else:
            counted = 0
            count = 0

    return largestcount
        


if __name__ == '__main__':
    import doctest
    doctest.testmod()
