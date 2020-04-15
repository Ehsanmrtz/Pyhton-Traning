while True:
    word = input("input word = ")
    v = ["a", "e", "i", "o", "u"]
    found = {}
    
    for letter in word:
        if letter in v:
            found.setdefault(letter, 0)
            found[letter] += 1
    for k, v in found.items():
            print(k, 'Was Found', v, 'times(s).')
