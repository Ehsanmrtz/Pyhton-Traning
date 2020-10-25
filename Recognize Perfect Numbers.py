# Recognize perfect numbers
number = int(input('Enter Your Number(number>0): '))
if number <= 0:
    print('Your number in not in our valid range please try again')
i_total = 0
for i in range(1,number):
    if number % i == 0:
        i_total += i
if i_total == number:
    print('Your number is a perfect number')
else:
    print('Your number is not a perfect number')