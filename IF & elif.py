age = int(input('Enter Your age: '))
if age < 0:
    print ('Enter correct number')
elif age > 0 and age < 6:
    print ('Khordsal')
elif age >= 6 and age < 10:
    print ('Koodak')
elif age >= 10 and age < 14:
    print ('Nojavan')
elif age >= 14 and age < 24:
    print ('Javan')
elif age >= 24 and age < 40:
    print ('Bozorgsal')
elif age >= 40:
    print ('Miansal')