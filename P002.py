while True:
    word = input("input word = ")
    v = ["a", "e", "i", "o", "u"]
    found = {}
<<<<<<< HEAD
    found['a'] = 0
    found['e'] = 0
    found['i'] = 0
    found['o'] = 0
    found['u'] = 0

    for letter in word:
        if letter in v:
            found[letter] += 1
    for k, v in found.items():
        print(k, 'Was Found', v, 'times(s).')
=======
    
    for letter in word:
        if letter in v:
            found.setdefault(letter, 0)
            found[letter] += 1
    for k, v in found.items():
            print(k, 'Was Found', v, 'times(s).')
>>>>>>> 2c1acf09c943c494072ca06f97f9d71c3a386ac7
