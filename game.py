import random
cn = random.randint(1,100)
person_number = int(input('Enter Your Number : '))
while person_number != cn:
    if cn > person_number:
        print ('Your number is Smaller')
        person_number = int(input('Enter Your Number : '))
    else:
        print ('Your Numebr is Bigger')
        person_number = int(input('Enter Your Number : '))
print (' WooooW You Are Smart')