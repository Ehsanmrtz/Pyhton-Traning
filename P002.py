while True:
    word = input("input word = ")
    v = ["a", "e", "i", "o", "u"]
    found = {}
    found['a'] = 0
    found['e'] = 0
    found['i'] = 0
    found['o'] = 0
    found['u'] = 0

    for letter in word:
        if letter in v:
            found[letter] += 1
    for k, v in found.items():
        if v > 0:
            print(k, 'Was Found', v, 'times(s).')
