while True:
    word = input("input word = ")
    v = ["a", "e", "i", "o", "u"]
    found = []
    for letter in word:
        if letter in v:
            if letter not in found:
                found.append(letter)
    for vowel in found:
            print(vowel)
        
