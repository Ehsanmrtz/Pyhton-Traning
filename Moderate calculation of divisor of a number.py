# Moderate of divisor of a number
number = int(input('Enter a number: '))
count = 0
t = 0
for i in range (1,number+1):
    if number % i == 0:
        t += i
        count += 1
cal = t / count
print ('Moderate of the divisor numbers is: ',cal)