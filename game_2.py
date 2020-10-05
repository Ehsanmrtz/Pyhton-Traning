# This is a numerical game
import random
pc_n = random.randint(0,20)
print ('Computer Sugguestion is :',pc_n)
user_answer = input('Choose one of the answers(Yes, Smaller, Bigger):')
while user_answer != 'Yes':
    if user_answer == 'Bigger':
        pc_n = random.randint(pc_n,20)
        print ('Computer Sugguestion is :',pc_n)
        user_answer = input('Choose one of the answers(Yes, Smaller, Bigger):')
    else:
        pc_n = random.randint(0,pc_n)
        print ('Computer Sugguestion is :',pc_n)
        user_answer = input('Choose one of the answers(Yes, Smaller, Bigger):')
if user_answer == 'Yes':
        print ('Yes, That is the number')
            
