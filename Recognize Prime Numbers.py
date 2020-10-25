# Recognize prime numbers
number = int(input('Enter Your Number: '))
if number <=1:
    print('Your number is not a prime number')
else:
    count = 0
    for i in range (2,number):
        if number % i == 0:
            count +=1
    if count>0:
        print('Your number is not a prime number')
            
    else:
        print('Your number is a prime number')