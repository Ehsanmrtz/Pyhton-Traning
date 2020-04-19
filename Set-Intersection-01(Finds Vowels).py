while True:
    word = input ('input word = ')
    vowels = set ('aeiou')
    i = vowels.intersection(set(word))
    vi = list(i)
    print('vowel word in your word are =',vi)
