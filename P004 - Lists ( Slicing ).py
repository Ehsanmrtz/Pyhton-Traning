# Use slicing to change the phrase
phrase = 'you can see the world'
question_type = phrase[8:]
question_type = phrase[4:8] + phrase[0:4] + question_type + ' ' + '?'
print('phrase = ',phrase)
print('question type = ',question_type)
new_word = list(phrase)
new_phrase = (phrase[4:8] + ' ' + phrase[0:4] + ' ' + phrase[4] + phrase[1] + phrase[-1]
              + ' ' + '?')
print('new phrase =', new_phrase)
