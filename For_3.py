# finding and counting a word in phrase
phrase = input('Enter Your Phrase: ')
word = input('Enter Your Word that you want to search: ')
count = 0
for i in phrase:
    if i == word:
        count = count + 1
print('We find %s number of %s in your phrase' % (count, word))